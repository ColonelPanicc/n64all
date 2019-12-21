package com.colonelpanic.n64all.server.service

import com.colonelpanic.n64all.server.model.ControllerProperty

interface PlayerController {
    fun setState(property: ControllerProperty?, value: Int)
    fun getState(property: ControllerProperty?): Int
}