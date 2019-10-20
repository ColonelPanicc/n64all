package com.colonelpanic.n64all.server.service;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static com.colonelpanic.n64all.server.model.ControllerProperty.ANALOG_X;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

public class ControllerServiceTest {

    private ControllerService sut;

    @BeforeEach
    public void setUp() {
        sut = new ControllerService();
    }

    @AfterEach
    public void tearDown() {
    }

    @Test
    public void shouldBarfIfStateUpdatedForUncreatedPlayer() {
        //given
        int playerId = 15;

        assertThrows(PlayerNotFoundException.class,
                () -> sut.updatePlayerState(playerId, ANALOG_X, 5));
    }

    @Test
    public void shouldBarfOnGetStateForUncreatedPlayer() {
        //given
        int playerId = 15;

        assertThrows(PlayerNotFoundException.class,
                () -> sut.getPlayerState(playerId, ANALOG_X));
    }

    @Test
    public void shouldUpdateStateForPrecreatedPlayer() {
        //given
        int playerId = 1;
        int stateValue = 5;
        sut.addPlayer(playerId);
        sut.updatePlayerState(playerId, ANALOG_X, 5);

        assertEquals(stateValue, sut.getPlayerState(playerId, ANALOG_X));
    }

}