import hug

from schema import Schema, And, Use, Optional, SchemaError

from bee import *
from input import Input, Analog
from input_types import InputTypes
from controller import Controller

NUM_CONTROLLERS = 4

controllers = {i: Controller() for i in range(NUM_CONTROLLERS)}


@hug.get('/state', output=hug.output_format.json)
def get_state(player: int=0):
    try:
        return controllers[player].get_state()
    except KeyError:
        return { 'Error' : "That's not a valid player my dude" }


player_schema = Schema(And(int, Use(int), lambda x: 0 <= x <= NUM_CONTROLLERS))
input_schema = Schema(And(str, Use(str), Use(str.upper), lambda x: x in [y.value for y in InputTypes]))
active_schema = Schema(Optional(bool))
angle_schema = Schema(And(Optional(float), Use(float), lambda  x: 0 <= x <= 360))
tilt_schema = Schema(And(Optional(float), Use(float), lambda  x: 0 <= x <= 1))

@hug.post('/update')
def update(player: int=0, input: str="", active: bool=None, angle: float=None, tilt: float=None):
    try:
        player = player_schema.validate(player)
        input = input_schema.validate(input)
        active = active_schema.validate(active)
        angle = angle_schema.validate(angle)
        tilt = tilt_schema.validate(tilt)
    except SchemaError as e:
        print(e)
        return {'Error' : str(e)}

    controller = controllers[player]
    input = controller.get_button(input)

    if isinstance(input, Analog):
        if angle:
            input.set_angle(angle)

        if tilt:
            input.set_tilt(tilt)

    if active:
        input.set_active(active)



@hug.get('/test', output=hug.output_format.text)
def test():
    return bee
