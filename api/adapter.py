from controller import Controller
from input_types import InputTypes


CONTROLLER_TO_OLLIE_CONVERSION = {
    "START" : "START_BUTTON",
    "C_UP_ARR" : "U_CBUTTON",
    "D_L_ARR" : "L_DPAD",
    "A_BTN" : "A_BUTTON",
    "B_BTN" : "B_BUTTON",
    "C_L_ARR" : "L_CBUTTON",
    "C_R_ARR" : "R_CBUTTON",
    "R_TRIGGER" : "R_TRIG",
    "D_R_ARR" : "R_DPAD",
    "C_D_ARR" : "D_CBUTTON",
    "Z_BTN" : "Z_TRIG",
    "L_TRIGGER" : "L_TRIG",
    "D_UP_ARR" : "U_DPAD",
    "D_D_ARR" : "D_DPAD"
}


class MikeAdapter:

    def __init__(self):
        pass

    @staticmethod
    def convert(raw_player: dict, c: Controller) -> None:

        c.get_button(InputTypes.ANALOG).set_x_y(*raw_player["ANALOG"])

        c.get_button(InputTypes.A_BUTTON).set_active(raw_player["A_BTN"] == 1)
        c.get_button(InputTypes.B_BUTTON).set_active(raw_player["B_BTN"] == 1)
        c.get_button(InputTypes.Z_BUTTON).set_active(raw_player["Z_BTN"] == 1)

        c.get_button(InputTypes.C_UP_ARROW).set_active(raw_player["C_UP_ARROW"] == 1)
        c.get_button(InputTypes.C_LEFT_ARROW).set_active(raw_player["C_LEFT_ARROW"] == 1)
        c.get_button(InputTypes.C_RIGHT_ARROW).set_active(raw_player["C_RIGHT_ARROW"] == 1)
        c.get_button(InputTypes.C_DOWN_ARROW).set_active(raw_player["C_DOWN_ARROW"] == 1)

        c.get_button(InputTypes.LEFT_TRIGGER).set_active(raw_player["L_TRIGGER"] == 1)
        c.get_button(InputTypes.RIGHT_TRIGGER).set_active(raw_player["R_TRIGGER"] == 1)

        c.get_button(InputTypes.START).set_active(raw_player["START"] == 1)



class OllieAdapter:

    def __init__(self):
        pass

    @staticmethod
    def convert(state):
        new_state = {}
        for id, s in state.items():
            if id in CONTROLLER_TO_OLLIE_CONVERSION:
                new_state[CONTROLLER_TO_OLLIE_CONVERSION[id]] = int(s['active'])
            elif id == InputTypes.ANALOG.name:
                new_state['X_AXIS'] = int(s['x'])
                new_state['Y_AXIS'] = int(s['y'])
        return new_state


