package com.colonelpanic.n64all.server

import com.colonelpanic.n64all.server.model.ControllerState
import com.colonelpanic.n64all.server.service.PlayerController

class StateFactory {
    fun create(): PlayerController {
        return ControllerState()
    }
}