package com.colonelpanic.n64all.server.model

enum class ControllerProperty
/**
 * The definition of the schema for each player controller property. This defines
 * defaults, as well as the allowed values.
 *
 * @param defaultValue the default value that this property is set to
 * @param min          the minimum value (inclusive) the property can be
 * @param max          the maximum value (inclusive) the property can be
 */(val defaultValue: Int, val minValue: Int, val maxValue: Int) {
    ANALOG_X(0, -80, 80), ANALOG_Y(0, -80, 80), A_BTN(0, 0, 1), B_BTN(0, 0, 1), Z_BTN(0, 0, 1), C_UP_ARROW(0, 0, 1), C_LEFT_ARROW(0, 0, 1), C_RIGHT_ARROW(0, 0, 1), C_DOWN_ARROW(0, 0, 1), L_TRIGGER(0, 0, 1), R_TRIGGER(0, 0, 1), START(0, 0, 1);

}