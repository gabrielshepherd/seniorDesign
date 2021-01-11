from flask import Flask, request
app = Flask(__name__)

from random import random

@app.route('/')
def hello_world():
    return "my name jeff"

@app.route('/echo')
def echo():
    return request.json

@app.route('/light_on')
def light_on():
    location = request.json['location']
    color = request.json['color']
    # andrew do your thing
    return