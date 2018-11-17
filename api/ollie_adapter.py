from input_types import InputTypes


BUTTON_KEYWORD_CONVERSION = {
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


class OllieAdapter:

    def __init__(self):
        pass

    @staticmethod
    def convert(state):
        new_state = {}
        for id, s in state.items():
            if id in BUTTON_KEYWORD_CONVERSION:
                new_state[BUTTON_KEYWORD_CONVERSION[id]] = int(s['active'])
            elif id == InputTypes.ANALOG.name:
                new_state['X_AXIS'] = int(s['x'])
                new_state['Y_AXIS'] = int(s['y'])
        return new_state


