import json
import keyboard
import requests
import sys

SERVER_ADDRESS = "http://10.245.30.44:8000/"
STATE_SERVER_JOIN_ROUTE = SERVER_ADDRESS + "join"
STATE_SERVER_LEAVE_ROUTE = SERVER_ADDRESS + "leave"
STATE_SERVER_UPDATE_ROUTE = SERVER_ADDRESS + "update"


def handle_keyboard(keyboardEvent: keyboard.KeyboardEvent):

    state = {
        "ANALOG": (0, 0),
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

    requests.post(STATE_SERVER_UPDATE_ROUTE, json.dumps({PLAYER: state}))

    if keyboardEvent.name == "up":
        state["ANALOG"] = (0, 127)

    if keyboardEvent.name in ["a", "left"]:
        state["ANALOG"] = (-127, 0)

    if keyboardEvent.name == "down":
        state["ANALOG"] = (0, -127)

    if keyboardEvent.name in ["d", "right"]:
        state["ANALOG"] = (127, 0)

    if keyboardEvent.name == "w":
        state["A_BTN"] = 1

    if keyboardEvent.name == "s":
        state["B_BTN"] = 1

    if keyboardEvent.name == "q":
        state["Z_BTN"] = 1

    if keyboardEvent.name == "c":
        state["C_UP_ARROW"] = 1

    if keyboardEvent.name == "space":
        state["START"] = 1

    requests.post(STATE_SERVER_UPDATE_ROUTE, json.dumps({PLAYER: state}))



PLAYER = int(json.loads(requests.get(STATE_SERVER_JOIN_ROUTE).text).get("success", -1))

keyboard.hook(handle_keyboard)

while True:
    pass


