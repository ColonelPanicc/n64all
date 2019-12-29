package com.colonelpanic.n64all.server.service

import com.colonelpanic.n64all.server.StateFactory
import com.colonelpanic.n64all.server.model.ControllerProperty.ANALOG_X
import org.junit.jupiter.api.AfterEach
import org.junit.jupiter.api.Assertions
import org.junit.jupiter.api.BeforeEach
import org.junit.jupiter.api.Test

class ControllerServiceTest {
    private val stateProvider = StateFactory()
    private var sut: ControllerService? = null

    @BeforeEach
    fun setUp() {
        sut = ControllerService(stateProvider)
    }

    @AfterEach
    fun tearDown() {
    }

    @Test
    fun shouldBarfIfStateUpdatedForUncreatedPlayer() {
        val playerId = 15

        Assertions.assertThrows(PlayerNotFoundException::class.java) {
            sut!!.updatePlayerState(playerId, ANALOG_X, 5)
        }
    }

    @Test
    fun shouldBarfOnGetStateForUncreatedPlayer() {
        val playerId = 15

        Assertions.assertThrows(PlayerNotFoundException::class.java) {
            sut!!.getPlayerState(playerId, ANALOG_X)
        }
    }

    @Test
    fun shouldUpdateStateForPrecreatedPlayer() {
        val playerId = 1
        val stateValue = 5

        sut!!.addPlayer(playerId)
        sut!!.updatePlayerState(playerId, ANALOG_X, 5)

        Assertions.assertEquals(stateValue, sut!!.getPlayerState(playerId, ANALOG_X))
    }
}