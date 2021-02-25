from flask import Flask, request
from multiprocessing import Process
import time

app = Flask(__name__)

def function_call(location):
    # Andrew, this is where your stuff should go
    print(location)
    return

@app.route('/')
def connect():
    return "connection confirmed"

@app.route('/transmit')
def receive_data():
    location = request.json['location']
    function_call(location)
    return "data received"

@app.before_request
def before_request_func():
    msg = "before request"
    print(msg)
    return msg

# @app.after_request
@app.teardown_request
def after_request_func():
    msg = "after request"
    print(msg)
    return msg

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')