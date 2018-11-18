class State:
    def __init__(self, player):
        self.player = player
        self.state = {
            player :{
                "ANALOG": (0,0),
                "A_BTN": 0,
                "B_BTN": 0,
                "Z_BTN": 0,
                "C_UP_ARROW": 0,
                "C_LEFT_ARROW": 0,
                "C_RIGHT_ARROW": 0,
                "C_DOWN_ARROW": 0,
                "L_TRIGGER": 0,
                "R_TRIGGER": 0,
                "START": 0,
            }
        }

    def get_state(self):
        return self.state