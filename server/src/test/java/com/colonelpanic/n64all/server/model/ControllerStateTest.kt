package com.colonelpanic.n64all.server.model

import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.Test
import java.util.*

internal class ControllerStateTest {
    private var sut: ControllerState? = ControllerState()

    @Test
    fun shouldSetStateCorrectlyForValidValue() {
        val randGen = Random()
        for (i in 0 until NUMBER_OF_TRIALS) {
            val property = givenRandomControllerProperty(randGen)
            val expectedValue = randGen.nextInt(property.maxValue - property.minValue) + property.minValue

            // When
            sut!!.setState(property, expectedValue)

            // Then
            assertEquals(expectedValue, sut!!.getState(property))
        }
    }

    @Test
    fun shouldNotSetStateForInvalidValue() {
        // Given
        val invalidValue = 1000

        for (prop in ControllerProperty.values()) {

            // When
            sut!!.setState(prop, invalidValue)

            // Then
            assertEquals(prop.defaultValue, sut!!.getState(prop))
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