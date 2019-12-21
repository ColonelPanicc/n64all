package com.colonelpanic.n64all.server.model

import com.colonelpanic.n64all.server.service.PlayerController
import com.google.common.collect.Maps
import org.slf4j.LoggerFactory

class ControllerState : PlayerController {
    private val properties: MutableMap<ControllerProperty, Int>

    private fun isValidPropertyValue(prop: ControllerProperty, value: Int): Boolean {
        return prop.minValue <= value && prop.maxValue >= value
    }

    companion object {
        private val logger = LoggerFactory.getLogger(ControllerState::class.java)
    }

    init {
        properties = Maps.newConcurrentMap()
        for (prop in ControllerProperty.values()) {
            setState(prop, prop.defaultValue)
        }
    }

    override fun setState(property: ControllerProperty?, value: Int) {
        if (isValidPropertyValue(property!!, value)) {
            properties[property] = value
        }
    }

    override fun getState(property: ControllerProperty?): Int {
        return properties[property]!!
    }
}