from input_types import InputTypes
from input import Input, Analog


class Controller:

    def __init__(self):
        self._buttons = {
            InputTypes.ANALOG.value: Analog(),

            InputTypes.LEFT_TRIGGER.value: Analog(),
            InputTypes.RIGHT_TRIGGER.value: Analog(),

            InputTypes.A_BUTTON.value: Input(),
            InputTypes.B_BUTTON.value: Input(),
            InputTypes.Z_BUTTON.value: Input(),

            InputTypes.C_UP_ARROW.value: Input(),
            InputTypes.C_LEFT_ARROW.value: Input(),
            InputTypes.C_RIGHT_ARROW.value: Input(),
            InputTypes.C_DOWN_ARROW.value: Input(),

            InputTypes.D_UP_ARROW.value: Input(),
            InputTypes.D_LEFT_ARROW.value: Input(),
            InputTypes.D_RIGHT_ARROW.value: Input(),
            InputTypes.D_DOWN_ARROW.value: Input(),

            InputTypes.START.value: Input(),
        }

    def get_button(self, button):
        if isinstance(button, InputTypes):
            return self._buttons.get(button.value, None)
        elif isinstance(button, str):
            return self._buttons.get(button, None)

    def get_state(self):
        return {i: s.get_state() for i, s in self._buttons.items()}

