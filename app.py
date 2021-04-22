from flask import Flask, request
from LEDs.led_location import rainbow_cycle, snake, clear, part_location
from LEDs.led_animation import theater_mode, random_box
from threading import Thread, Event
import time


# init flask app
app = Flask(__name__)

#Creates a thread to have an idle mode
class MyThread(Thread):
    WAIT_TIME = 10000                        # in 10s of milliseconds

    def __init__(self, event):
        Thread.__init__(self)
        self.stopped = event

    def run(self):
        # Sleep for [time period]
        for i in range(MyThread.WAIT_TIME):
            if self.stopped.wait(0.001):
                return
        
        # Do the animation
        clear()
        j = 0 
        a = 0
        b = 457
        c = 318
        d = 563
        e = 137
        f = 669
        g = 288
        h = 274

        count = 0
        clears = 0
        color = 'green'

       # variable for rainbow cycle
        rainbow = 0
        while not self.stopped.wait(0.001):

            # Runs the rainbow cycle
            if rainbow < 2:
                rainbow_cycle(0.02, j)
                if j == 255:
                    j = 0
                    rainbow +=1
                    clears += 1
                else:
                    j += 1

            if clears == 2:
                clear()
                clears = 0
                count = 0

            # Runs the snake cycle
            if rainbow == 2:
                snake(a, color)
                a+=1
            if a == 122:
                rainbow +=1
                snake(b, color)
                b += 1
            if b == 563:
                a = 0
                snake(c, color)
                c -= 1
            if c == 303:
                b = 457
                snake(d, color)
                d += 1
            if d == 669:
                c = 318
                snake(e, color)
                e += 1
            if e == 152:
                d = 563
                snake(f, color)
                f += 1
            if f == 775:
                e = 137
                snake(g, color)
                g -= 1
            if g == 273:
                f = 669
                snake(h, color)
                h -= 1
            if h == 168:
                g = 288
                h = 274
                rainbow = 0
            


# Reads from the GUI
def function_call(location):
    clear()
    if location == 'animation1':
        theater_mode()
    if location == 'animation2':
        random_box()
    # if location == 'animation2':
    # if location == 'animation3':
    # if locaiton == 'animation4':
        
    part_location(location)
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