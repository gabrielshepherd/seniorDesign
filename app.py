from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def connect():
    return "connection established"

@app.route('/transmit')
def receive_data():
    location = request.json['location']
    color = request.json['color']
    print(location)
    print(color)
    return "data received"