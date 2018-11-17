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


class Input:

    def __init__(self):
        self._hold_time = 0
        self._active = False

    def get_held_time(self) -> int:
        return self._hold_time

    def toggle(self) -> None:
        self._active = not self._active

    def set_active(self, new_active) -> None:
        self._active = new_active

    def set_hold_time(self, new_hold_time) -> None:
        self._hold_time = new_hold_time


class Analog(Input):

    def __init__(self):
        super().__init__()
        self._angle, self._oomph = 0, 0

    def get_angle(self) -> int:
        return self._angle

    def get_oomph(self) -> int:
        return self._oomph

    def set_angle(self, new_angle) -> None:
        self._angle = new_angle

    def set_oomph(self, new_oomph) -> None:
        self._oomph = new_oomph


class Controller:

    def __init__(self):
        self._buttons = {
            InputTypes.LEFT_ANALOG: Analog(),
            InputTypes.RIGHT_ANALOG: Analog(),

            InputTypes.LEFT_TRIGGER: Analog(),
            InputTypes.RIGHT_TRIGGER: Analog(),

            InputTypes.A_BUTTON: Input(),
            InputTypes.B_BUTTON: Input(),
            InputTypes.Z_BUTTON: Input(),

            InputTypes.UP_ARROW: Input(),
            InputTypes.LEFT_ARROW: Input(),
            InputTypes.RIGHT_ARROW: Input(),
            InputTypes.DOWN_ARROW: Input(),

            InputTypes.START: Input(),
        }

