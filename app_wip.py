from flask import Flask, request
import multiprocessing as mp
import time
import queue

app = Flask(__name__)
running_flag = mp.Value("i", 1)
q = mp.Queue()

def function_call(location, t0):
    t1 = time.time()
    dt = t1 - t0
    while dt < 10:
        
    print(location)
    return

@app.route('/')
def connect():
    return "connection confirmed"

@app.route('/transmit')
def receive_data():
    t0 = time.time()
    location = request.json['location']
    function_call(location, t0)
    return "data received"