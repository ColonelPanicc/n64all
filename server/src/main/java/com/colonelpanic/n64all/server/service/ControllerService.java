package com.colonelpanic.n64all.server.service;

import com.colonelpanic.n64all.server.model.ControllerProperty;
import com.colonelpanic.n64all.server.model.ControllerState;
import com.google.common.collect.Maps;
import com.google.inject.Singleton;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.Map;

@Singleton
public class ControllerService {
    private static final Logger logger = LoggerFactory.getLogger(ControllerService.class);
    private Map<Integer, PlayerController> players;

    public ControllerService() {
        players = Maps.newConcurrentMap();
    }

    public void addPlayer(int playerId) {

        if(players.containsKey(playerId))
            return;

        // TODO use a Guice supplied Factory to get the appropriate state.
        players.put(playerId, new ControllerState());
    }
    public void updatePlayerState(int playerId, ControllerProperty propToUpdate, int valueToSet) {
        if(this.players.get(playerId) == null) {
            logger.error("Player with id: {} not found.", playerId);
            throw new PlayerNotFoundException();
        }
        this.players.get(playerId).setState(propToUpdate, valueToSet);
    }

    public int getPlayerState(int playerId, ControllerProperty property) {
        if(this.players.get(playerId) == null) {
            logger.error("Player with id: {} not found.", playerId);
            throw new PlayerNotFoundException();
        }
        return this.players.get(playerId).getState(property);
    }
}
