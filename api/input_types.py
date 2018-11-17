from enum import Enum

class InputTypes(Enum):

    LEFT_ANALOG = "L_ANALOG"
    RIGHT_ANALOG = "R_ANALOG"

    LEFT_TRIGGER = "L_TRIGGER"
    RIGHT_TRIGGER = "R_TRIGGER"

    A_BUTTON = "A_BTN"
    B_BUTTON = "B_BTN"
    Z_BUTTON = "Z_BTN"

    UP_ARROW = "UP_ARR"
    LEFT_ARROW = "L_ARR"
    RIGHT_ARROW = "R_ARR"
    DOWN_ARROW = "D_ARR"

    START = "START"