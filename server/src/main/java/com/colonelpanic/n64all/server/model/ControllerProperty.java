package com.colonelpanic.n64all.server.model;

public enum ControllerProperty {
    ANALOG_X(0, -80, 80),
    ANALOG_Y(0, -80, 80),
    A_BTN(0, 0, 1),
    B_BTN(0, 0, 1),
    Z_BTN(0, 0, 1),
    C_UP_ARROW(0, 0, 1),
    C_LEFT_ARROW(0, 0, 1),
    C_RIGHT_ARROW(0, 0, 1),
    C_DOWN_ARROW(0, 0, 1),
    L_TRIGGER(0, 0, 1),
    R_TRIGGER(0, 0, 1),
    START(0, 0, 1);

    private final int defaultValue;
    private final int minValue;
    private final int maxValue;

    /**
     * The definition of the schema for each player controller property. This defines
     * defaults, as well as the allowed values.
     *
     * @param defaultValue the default value that this property is set to
     * @param min          the minimum value (inclusive) the property can be
     * @param max          the maximum value (inclusive) the property can be
     */
    ControllerProperty(int defaultValue, int min, int max) {
        this.defaultValue = defaultValue;
        this.minValue = min;
        this.maxValue = max;
    }

    public int getDefaultValue() {
        return defaultValue;
    }

    public int getMinValue() {
        return minValue;
    }

    public int getMaxValue() {
        return maxValue;
    }
}
