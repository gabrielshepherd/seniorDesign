from flask import Flask, request
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