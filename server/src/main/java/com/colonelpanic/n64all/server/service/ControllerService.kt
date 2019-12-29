package com.colonelpanic.n64all.server.service

import com.colonelpanic.n64all.server.StateFactory
import com.colonelpanic.n64all.server.model.ControllerProperty
import com.google.common.collect.Maps
import com.google.inject.Inject
import com.google.inject.Singleton
import org.slf4j.Logger
import org.slf4j.LoggerFactory

@Singleton
class ControllerService @Inject constructor(private val stateProvider: StateFactory) {
    private val players: MutableMap<Int, PlayerController?>

    fun addPlayer(playerId: Int) {
        if (players.containsKey(playerId)) return

        players[playerId] = stateProvider.create()
    }

    fun updatePlayerState(playerId: Int, propToUpdate: ControllerProperty?, valueToSet: Int) {
        if (players[playerId] == null) {
            logger.error("Player with id: {} not found.", playerId)
            throw PlayerNotFoundException()
        }
        players[playerId]!!.setState(propToUpdate, valueToSet)
    }

    fun getPlayerState(playerId: Int, property: ControllerProperty?): Int {
        if (players[playerId] == null) {
            logger.error("Player with id: {} not found.", playerId)
            throw PlayerNotFoundException()
        }
        return players[playerId]!!.getState(property)
    }

    companion object {
        var logger: Logger = LoggerFactory.getLogger(this::class.java)
    }

    init {
        players = Maps.newConcurrentMap()
    }
}