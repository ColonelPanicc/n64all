from flask import Flask, render_template, request, url_for, redirect, make_response
import json

app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY'] = 'georgepricehasaf'


@app.route('/')
def login():
    return render_template('index.html')


@app.route('/acc', methods=['POST'])
def acc():
    forward = json.loads(request.data)
    forward = request.data['alpha']
    # beta = request.data['beta']
    # gamma = request.data['gamma']
    print(forward)
    return json.dumps(request.json)

if __name__ == '__main__':
    print('hello')
    app.run(debug=True, host='10.245.101.226', port=5000)

