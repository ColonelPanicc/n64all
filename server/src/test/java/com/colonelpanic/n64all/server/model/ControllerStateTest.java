package com.colonelpanic.n64all.server.model;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.Random;

import static org.junit.jupiter.api.Assertions.*;

class ControllerStateTest {
    private static final int NUMBER_OF_TRIALS = 15;
    private ControllerState sut;

    @BeforeEach
    void setUp() {
        sut = new ControllerState();
    }

    @AfterEach
    void tearDown() {
    }

    @Test
    public void shouldSetStateCorrectlyForValidValue() {
        Random randGen = new Random();

        for (int i = 0; i < NUMBER_OF_TRIALS; i++) {
            ControllerProperty p = givenRandomControllerProperty(randGen);
            int expectedValue = randGen.nextInt(p.getMaxValue() - p.getMinValue()) + p.getMinValue();

            sut.setState(p, expectedValue);
            assertEquals(expectedValue, sut.getState(p));
        }
    }

    @Test
    public void shouldNotSetStateForInvalidValue() {
        int invalidValue = 1000;

        for(ControllerProperty prop : ControllerProperty.values()) {
            sut.setState(prop, invalidValue);
            assertEquals(prop.getDefaultValue(), sut.getState(prop));
        }
    }

    private ControllerProperty givenRandomControllerProperty(Random randGen) {
        ControllerProperty[] props = ControllerProperty.values();
        return props[randGen.nextInt(props.length)];
    }

}