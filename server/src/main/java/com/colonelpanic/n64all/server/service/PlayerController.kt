package com.colonelpanic.n64all.server.service

import com.colonelpanic.n64all.server.model.ControllerProperty

/**
Provides an implementation of a player controller,
used to set and get state.
 */
interface PlayerController {
    /**
     * Set the state of the Player Controller.
     *
     * @param property the property to set
     * @param value the value of the property (as an Integer)
     */
    fun setState(property: ControllerProperty?, value: Int)

    /**
     * Get the state of a given property within the Player Controller.
     *
     * @param property the property to retrieve the value of
     */
    fun getState(property: ControllerProperty?): Int
}