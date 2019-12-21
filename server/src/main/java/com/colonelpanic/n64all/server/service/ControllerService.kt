package com.colonelpanic.n64all.server.service

import com.colonelpanic.n64all.server.model.ControllerProperty
import com.colonelpanic.n64all.server.model.ControllerState
import com.google.common.collect.Maps
import com.google.inject.Singleton
import org.slf4j.LoggerFactory

@Singleton
class ControllerService {
    private val players: MutableMap<Int, PlayerController?>
    fun addPlayer(playerId: Int) {
        if (players.containsKey(playerId)) return
        // TODO use a Guice supplied Factory to get the appropriate state.
        players[playerId] = ControllerState()
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
        private val logger = LoggerFactory.getLogger(ControllerService::class.java)
    }

    init {
        players = Maps.newConcurrentMap()
    }
}