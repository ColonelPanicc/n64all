from flask import Flask, render_template, request, url_for, redirect, make_response
import json
import math
import requests
import threading
import random
import atexit
#
# def set_interval(func, sec):
#     def func_wrapper():
#         set_interval(func, sec)
#         func()
#     t = threading.Timer(sec, func_wrapper)
#     t.start()
#     return t

PLAYERS = 4
X_TOLERANCE = 15

global right
global PLAYER
right = 0
PLAYER = "-1"

app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY'] = 'georgepricehasaf'



@app.route('/')
def login():
    return render_template('index.html')




@app.route('/acc', methods=['POST'])
def acc():
    global right
    data = request.get_json()
    rt = data['alpha']

    if -X_TOLERANCE <= rt <= X_TOLERANCE:
        rt = 0

    right += rt * 0.05

    right = min(127, max(-127, int(right)))
        
    state = {
        str(PLAYER) :{
            "ANALOG": (right, 127),
            "A_BTN": random.random() < 0.85,
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

    # state[PLAYER]["ANALOG"] = (right, 127)
    # state[PLAYER]["A_BTN"] = random.random() < 0.99
    # state[PLAYER]["B_BTN"] = forward > 0

    send_to_api(state)

    # print('{} forward  {} right'.format(forward, right))
    return json.dumps(request.json)

def send_to_api(state):
    url = "http://localhost:8000/update"
    data_string = json.dumps(state)
    print(state)
    requests.post(url, data_string)

def join():
    output = requests.get("http://localhost:8000/join").json()

    if "success" in output:
        return output["success"]
    return -1

def leave():
    requests.post("http://localhost:8000/leave")

# set_interval(send_to_api, 0.25)

if __name__ == '__main__':
    print('hello')
    atexit.register(leave)
    PLAYER = join()
    app.run(debug=False, host='10.245.8.174', port=5000)

