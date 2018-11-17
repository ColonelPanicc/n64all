import pygame
import requests
import json

# noinspection PyUnresolvedReferences
from enums.Xbox360 import PyAxisMap, PyButtonMap, PyHatMap

STATE_SERVER_UPDATE_ROUTE = "http://0d5334d4.ngrok.io/update"
TARGET_UPDATES_PER_SECOND = 1

ANALOG_CONVERSION_FACTOR = 127


def get_input_data_object(js):
    hat = js.get_hat(PyHatMap.DPAD.value)
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

    joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
    for js in joysticks:
        js.init()
    joysticks = [x for x in joysticks if "xbox gamepad" in x.get_name().lower()]

    if len(joysticks) > 0:
        js = joysticks[0]
        print("Joystick 0 info -- Buttons: {} Axes: {} Hats: {}".format(js.get_numbuttons(), js.get_numaxes(),
                                                                        js.get_numhats()))

    done = False
    while not done:
        pygame.event.pump()
        data_to_send = {}

        for js_id, js in enumerate(joysticks):
            data_to_send[js_id] = get_input_data_object(js)

            if js.get_button(PyButtonMap.XBOX_HOME.value):
                done = True
                continue

        data_string = json.dumps(data_to_send)
        print("\r{}".format(data_string), end="")
        requests.post(STATE_SERVER_UPDATE_ROUTE, data_string)

        clock.tick(TARGET_UPDATES_PER_SECOND)

    pygame.joystick.quit()


if __name__ == '__main__':
    main()
