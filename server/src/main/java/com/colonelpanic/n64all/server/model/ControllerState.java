package com.colonelpanic.n64all.server.model;

import com.colonelpanic.n64all.server.service.PlayerController;
import com.google.common.collect.Maps;

import java.util.Map;

public class ControllerState implements PlayerController {
    private Map<ControllerProperty, Integer> properties;

    public ControllerState() {
        this.properties = Maps.newConcurrentMap();

        for (ControllerProperty prop : ControllerProperty.values()) {
            setState(prop, prop.getDefaultValue());
        }
    }

    public void setState(ControllerProperty property, int value) {
        if (isValidPropertyValue(property, value)) {
            properties.put(property, value);
        }
    }

    public int getState(ControllerProperty property) {
        return properties.get(property);
    }

    private boolean isValidPropertyValue(ControllerProperty prop, int value) {
        return prop.getMinValue() <= value && prop.getMaxValue() >= value;
    }
}
