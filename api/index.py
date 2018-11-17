import hug

from schema import Schema, And, Use, Optional, SchemaError

from bee import *
from input import Input, Analog
from input_types import InputTypes
from json import loads
from controller import Controller
from adapter import MikeAdapter, OllieAdapter

NUM_CONTROLLERS = 4


ollie_adapter = OllieAdapter()
controllers = {i: Controller() for i in range(NUM_CONTROLLERS)}


@hug.get('/state', output=hug.output_format.json)
def get_state(player: int=0):
    try:
        return ollie_adapter.convert(controllers[player].get_state())
    except KeyError:
        return { 'Error' : "That's not a valid player my dude" }


player_schema = Schema(And(int, Use(int), lambda x: 0 <= x <= NUM_CONTROLLERS))
input_schema = Schema(And(str, Use(str), Use(str.upper), lambda x: x in [y.value for y in InputTypes]))
active_schema = Schema(Optional(bool))
angle_schema = Schema(And(Optional(int), Use(int), lambda  x: -80 <= x <= 80))
tilt_schema = Schema(And(Optional(int), Use(int), lambda  x: -80 <= x <= 80))

"""
@hug.post('/update')
def update(player: int=0, input: str="", active: bool=None, x: int=None, y: int=None):
    try:
        player = player_schema.validate(player)
        input = input_schema.validate(input)
        active = active_schema.validate(active)
        x = angle_schema.validate(x)
        y = tilt_schema.validate(y)
    except SchemaError as e:
        print(e)
        return {'Error' : str(e)}

    controller = controllers[player]
    input = controller.get_button(input)

    if isinstance(input, Analog):
        if x:
            input.set_x(x)

        if y:
            input.set_y(y)

    if active:
        input.set_active(active)
        """


@hug.post('/update')
def update(body):

    formatted_body = loads(body)

    for player in formatted_body:
        print(player)
        controllers[int(player)] = MikeAdapter().convert(formatted_body[player])

    print(controllers)

    return ";) X"


@hug.get('/test', output=hug.output_format.text)
def test():
    return bee
