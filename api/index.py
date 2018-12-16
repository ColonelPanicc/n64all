import hug

from schema import Schema, And, Use, Optional, SchemaError

from bee import *
from input import Input, Analog
from input_types import InputTypes
from json import loads
import json
from controller import Controller
from adapter import MikeAdapter, OllieAdapter

NUM_CONTROLLERS = 4

api = hug.API(__name__)
api.http.add_middleware(hug.middleware.CORSMiddleware(api, max_age=10))


ollie_adapter = OllieAdapter()
controllers = {i: Controller() for i in range(NUM_CONTROLLERS)}
players = [False for i in range(NUM_CONTROLLERS)]


@hug.get('/state', output=hug.output_format.text)
def get_state(player: int=0):
    try:
        state = ollie_adapter.convert(controllers[player].get_state())
        s = json.dumps(state)
        s = s.replace("\'","\"")
        print(s)
        return s
    except KeyError:
        return { 'Error' : "That's not a valid player my dude" }


player_schema = Schema(And(int, Use(int), lambda x: 0 <= x <= NUM_CONTROLLERS))
input_schema = Schema(And(str, Use(str), Use(str.upper), lambda x: x in [y.value for y in InputTypes]))
active_schema = Schema(Optional(bool))
angle_schema = Schema(And(Optional(int), Use(int), lambda  x: -80 <= x <= 80))
tilt_schema = Schema(And(Optional(int), Use(int), lambda  x: -80 <= x <= 80))


@hug.get('/join')
def join():
    for i, active in enumerate(players):
        if not active:
            players[i] = True
            return {"success": i}
    return {"error": -1}


@hug.post('/leave')
def leave(body):

    player_id = loads(body).get("player_id", -1)

    if player_id >= len(players) or player_id < 0:
        return {"error": "player id is not valid"}

    if not players[player_id]:
        return {"error": "player id has not been assigned yet"}

    players[player_id] = False

    return {"success": "player id has been kicked"}


@hug.post('/update')
def update(body):

    formatted_body = loads(body)

    for player in formatted_body:
        MikeAdapter().convert(formatted_body[player], controllers[int(player)])

    return ";) X"

@hug.static('/static')
def my_static_dirs():
    return ('./webpage_controller',)
