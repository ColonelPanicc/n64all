package com.colonelpanic.n64all.server.service

import com.colonelpanic.n64all.server.model.ControllerProperty
import org.junit.jupiter.api.AfterEach
import org.junit.jupiter.api.Assertions
import org.junit.jupiter.api.BeforeEach
import org.junit.jupiter.api.Test

class ControllerServiceTest {
    private var sut: ControllerService? = null
    @BeforeEach
    fun setUp() {
        sut = ControllerService()
    }

    @AfterEach
    fun tearDown() {
    }

    @Test
    fun shouldBarfIfStateUpdatedForUncreatedPlayer() { //given
        val playerId = 15
        Assertions.assertThrows(PlayerNotFoundException::class.java
        ) { sut!!.updatePlayerState(playerId, ControllerProperty.ANALOG_X, 5) }
    }

    @Test
    fun shouldBarfOnGetStateForUncreatedPlayer() { //given
        val playerId = 15
        Assertions.assertThrows(PlayerNotFoundException::class.java
        ) { sut!!.getPlayerState(playerId, ControllerProperty.ANALOG_X) }
    }

    @Test
    fun shouldUpdateStateForPrecreatedPlayer() { //given
        val playerId = 1
        val stateValue = 5
        sut!!.addPlayer(playerId)
        sut!!.updatePlayerState(playerId, ControllerProperty.ANALOG_X, 5)
        Assertions.assertEquals(stateValue, sut!!.getPlayerState(playerId, ControllerProperty.ANALOG_X))
    }
}