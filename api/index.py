import hug
from bee import *
from controller import Controller

NUM_CONTROLLERS = 4

controllers = {i : Controller() for i in range(NUM_CONTROLLERS)}

@hug.get('/state', output=hug.output_format.json)
def get_state(player_id:int=0):
    try:
        return controllers[player_id].get_state()
    except KeyError:
        return {
            'Error' : "That's not a valid player my dude"
        }


@hug.get('/test', output=hug.output_format.text)
def test():
    return bee
