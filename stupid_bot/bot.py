from helpers.controls import DirectionRandomGenerator
import math
import requests
import random

def send_state(x, y, a):
    state = {
        "ANALOG": (math.ceil(x),math.ceil(y)),
        "A_BTN": a,
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
    r = requests.post('http://localhost:8000', json=state)


def main():
    while True:
        direction_gen = DirectionRandomGenerator(-127, 127, -127, 127)
        a = random.randint(0,1)
        x, y = direction_gen.fetch_direction()
        send_state(x, y, a)



if __name__ == '__main__':
    main()