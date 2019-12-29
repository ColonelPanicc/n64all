package com.colonelpanic.n64all.server

import com.colonelpanic.n64all.server.model.ControllerState
import org.junit.jupiter.api.Test

import org.junit.jupiter.api.Assertions.*
import org.mockito.Matchers

internal class StateFactoryTest {
    val sut = StateFactory()
    @Test
    fun create() {
        val state = sut.create()

        assertTrue(state is ControllerState)
    }
}