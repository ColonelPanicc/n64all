import hug
from bee import *
from input import Input, Analog
from controller import Controller

NUM_CONTROLLERS = 4

controllers = {i : Controller() for i in range(NUM_CONTROLLERS)}

@hug.get('/state', output=hug.output_format.json)
def get_state(player:int=0):
    try:
        return controllers[player].get_state()
    except KeyError:
        return { 'Error' : "That's not a valid player my dude" }

@hug.post('/update')
def update(player:int=0, input:str="", active:bool=None, angle:float=None, tilt:float=None):
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
