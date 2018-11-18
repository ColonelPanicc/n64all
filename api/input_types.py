from enum import Enum


class InputTypes(Enum):
    ANALOG = "ANALOG"

    LEFT_TRIGGER = "L_TRIGGER"
    RIGHT_TRIGGER = "R_TRIGGER"

    A_BUTTON = "A_BTN"
    B_BUTTON = "B_BTN"
    Z_BUTTON = "Z_BTN"

    D_UP_ARROW = "D_UP_ARR"
    D_LEFT_ARROW = "D_L_ARR"
    D_RIGHT_ARROW = "D_R_ARR"
    D_DOWN_ARROW = "D_D_ARR"

    C_UP_ARROW = "C_UP_ARR"
    C_LEFT_ARROW = "C_L_ARR"
    C_RIGHT_ARROW = "C_R_ARR"
    C_DOWN_ARROW = "C_D_ARR"

    START = "START"
