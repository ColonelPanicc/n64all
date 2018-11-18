import pygame
import requests
import json
import time

# noinspection PyUnresolvedReferences
from enums.Xbox360 import PyAxisMap, PyButtonMap, PyHatMap

SERVER_ADDRESS = "http://10.245.8.174:8000/"
STATE_SERVER_JOIN_ROUTE = SERVER_ADDRESS + "join"
STATE_SERVER_LEAVE_ROUTE = SERVER_ADDRESS + "leave"
STATE_SERVER_UPDATE_ROUTE = SERVER_ADDRESS + "update"
TARGET_UPDATES_PER_SECOND = 300

ANALOG_CONVERSION_FACTOR = 127


def get_input_data_object(js):
    hat = js.get_hat(PyHatMap.DPAD.value)
    # get_hat is -1 for one direction, 1 for other, 0 for not pressed, converting this to individual buttons
    # get_button returns 1 for button pressed, 0 for not pressed
    return {
        "ANALOG": (
            round(ANALOG_CONVERSION_FACTOR * js.get_axis(PyAxisMap.LEFT_THUMB_X.value)),
            round(ANALOG_CONVERSION_FACTOR * js.get_axis(PyAxisMap.LEFT_THUMB_Y.value))),
        "A_BTN": js.get_button(PyButtonMap.A.value),
        "B_BTN": js.get_button(PyButtonMap.B.value),
        "Z_BTN": js.get_button(PyButtonMap.X.value),
        "C_UP_ARROW": 1 if hat[1] > 0 else 0,
        "C_LEFT_ARROW": 1 if hat[0] < 0 else 0,
        "C_RIGHT_ARROW": 1 if hat[0] > 0 else 0,
        "C_DOWN_ARROW": 1 if hat[1] < 0 else 0,
        "L_TRIGGER": js.get_button(PyButtonMap.LEFT_BUTTON.value),
        "R_TRIGGER": js.get_button(PyButtonMap.RIGHT_BUTTON.value),
        "START": js.get_button(PyButtonMap.START.value),
    }


def main():
    pygame.display.init()
    pygame.joystick.init()
    clock = pygame.time.Clock()

    js = pygame.joystick.Joystick(0)
    js.init()

    if "xbox gamepad" in js.get_name().lower():
        print("Joystick 0 info -- Buttons: {} Axes: {} Hats: {}".format(
            js.get_numbuttons(), js.get_numaxes(), js.get_numhats()))

        # Ask to join
        join_response = requests.get(STATE_SERVER_JOIN_ROUTE).text
        my_id = int(json.loads(join_response).get("success", -1))
        print("Received id: {}".format(my_id))

        # If join was successful, we have an id >= 0
        if my_id > -1:
            done = False
            request_count = 0

            while not done:
                last_time = time.time()
                pygame.event.pump()

                # Exit route with xbox home
                if js.get_button(PyButtonMap.XBOX_HOME.value):
                    done = True
                    continue

                data_to_send = {
                    my_id: get_input_data_object(js)
                }

                request_count += 1
                requests.post(STATE_SERVER_UPDATE_ROUTE, json.dumps(data_to_send))
                clock.tick(TARGET_UPDATES_PER_SECOND)

                elapsed = time.time() - last_time
                print("request number {} ({}ms request time)     ".format(
                    request_count, round(1000 * elapsed)),
                    end="\r")

            requests.post(STATE_SERVER_LEAVE_ROUTE, json.dumps({"player_id": my_id}))

    pygame.joystick.quit()


if __name__ == '__main__':
    main()
