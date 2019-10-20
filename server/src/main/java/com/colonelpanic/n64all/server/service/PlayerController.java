package com.colonelpanic.n64all.server.service;

import com.colonelpanic.n64all.server.model.ControllerProperty;

public interface PlayerController {
    void setState(ControllerProperty property, int value);

    int getState(ControllerProperty property);

}
