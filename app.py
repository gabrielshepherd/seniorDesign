from flask import Flask, request
from LEDs.led_location import rainbow_cycle, sectionB
from threading import Thread, Event
import time


# init flask app
app = Flask(__name__)

class MyThread(Thread):
    WAIT_TIME = 1000                        # in 10s of milliseconds

    def __init__(self, event):
        Thread.__init__(self)
        self.stopped = event

    def run(self):
        # Sleep for [time period]
        for i in range(MyThread.WAIT_TIME):
            if self.stopped.wait(0.01):
                return
        # Do the animation
        j = 0
        while not self.stopped.wait(0.01):
            # print(f"my thread ({count})")
            rainbow_cycle(0.01, j)
            if j == 255:
                j -= 255
            else:
                j += 1


def function_call(location):
    # Andrew, this is where your stuff should go
    if location == 'B3':
        sectionB()
    # if location == 'A':
    #     sectionA()
    # if location == 'B':
    #     sectionB()
    # if location == 'C':
    #     sectionC()
    # if location == 'D':
    #     sectionD()
    print(location)
    return


@app.route('/')
def connect():
    return "connection confirmed"


@app.route('/transmit')
def receive_data():
    global idle_thread

    # stop the idle animation thread
    stopFlag.set()
    idle_thread.join()

    # do the actual request handling stuff with the LEDs
    location = request.json['location']
    function_call(location)

    # Restart the idle animation thread
    stopFlag.clear()
    idle_thread = MyThread(stopFlag)
    idle_thread.start()

    return "thank you for sending " + location


if __name__ == '__main__':
    stopFlag = Event()
    idle_thread = MyThread(stopFlag)
    idle_thread.start()
    app.run(debug=False, host='0.0.0.0')