from helpers.controls import DirectionRandomGenerator
import math
import requests
import random
import json
import atexit

def leave():
    requests.post('http://localhost:8000/leave')

def send_state(player, x, y, a):
    state = {
        player: {
            "ANALOG": (math.ceil(x), math.ceil(y)),
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
    }
    r = requests.post('http://localhost:8000/update', json=json.dumps(state))

def join():
    output = requests.get('http://localhost:8000/join').json()
    if "success" in output:
        return output["success"]
    return -1

def main():
    player_num = join()
    while True:
        direction_gen = DirectionRandomGenerator(-80, 80, -25, 127)
        a = random.randint(0,1)
        x, y = direction_gen.fetch_direction()
        send_state(player_num, x, y, a)



if __name__ == '__main__':
    atexit.register(leave)
    main()