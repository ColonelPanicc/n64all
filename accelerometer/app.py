from flask import Flask, render_template, request, url_for, redirect, make_response
import json
import math

app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY'] = 'georgepricehasaf'


@app.route('/')
def login():
    return render_template('index.html')


@app.route('/acc', methods=['POST'])
def acc():
    data = json.loads(request.data)
    forward = data['gamma']
    right = data['beta']

    print('{} forward  {} right'.format(forward, right))
    return json.dumps(request.json)

def send_to_api():
    url = "http://localhost:8000/"

if __name__ == '__main__':
    print('hello')
    app.run(debug=True, host='10.245.101.226', port=5000)

