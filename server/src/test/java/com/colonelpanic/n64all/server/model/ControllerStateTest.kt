package com.colonelpanic.n64all.server.model

import org.junit.jupiter.api.AfterEach
import org.junit.jupiter.api.Assertions
import org.junit.jupiter.api.BeforeEach
import org.junit.jupiter.api.Test
import java.util.*

internal class ControllerStateTest {
    private var sut: ControllerState? = null
    @BeforeEach
    fun setUp() {
        sut = ControllerState()
    }

    @AfterEach
    fun tearDown() {
    }

    @Test
    fun shouldSetStateCorrectlyForValidValue() {
        val randGen = Random()
        for (i in 0 until NUMBER_OF_TRIALS) {
            val p = givenRandomControllerProperty(randGen)
            val expectedValue = randGen.nextInt(p.maxValue - p.minValue) + p.minValue
            sut!!.setState(p, expectedValue)
            Assertions.assertEquals(expectedValue, sut!!.getState(p))
        }
    }

    @Test
    fun shouldNotSetStateForInvalidValue() {
        val invalidValue = 1000
        for (prop in ControllerProperty.values()) {
            sut!!.setState(prop, invalidValue)
            Assertions.assertEquals(prop.defaultValue, sut!!.getState(prop))
        }
    }

    private fun givenRandomControllerProperty(randGen: Random): ControllerProperty {
        val props = ControllerProperty.values()
        return props[randGen.nextInt(props.size)]
    }

    companion object {
        private const val NUMBER_OF_TRIALS = 15
    }
}