from input_types import InputTypes
from input import Input, Analog


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

    def get_button(self, button):
        return self._buttons.get(button, None)

    def get_state(self):
        return {i.name: s.get_state() for i, s in self._buttons.items()}

