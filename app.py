from flask import Flask, request
from LEDs.led_location import rainbow_cycle, snake, clear, part_location, wheel
from threading import Thread, Event
import time


# init flask app
app = Flask(__name__)

#Creates a thread to have an idle mode
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
        clear()
        j = 0 
        
        # a = 0,122,1
        # b = 457,565,1
        # c = 318,303,-1
        # d = 566,671,1
        # e = 137,152,1
        # f = 672,777,1
        # g = 289,274,-1
        # h = 274,168,-1

        a = 0
        b = 457
        c = 318
        d = 566
        e = 137
        f = 672
        g = 289
        h = 274

         # variable for rainbow cycle
        rainbow = 0
        while not self.stopped.wait(0.01):
            # Runs the rainbow cycle
            if rainbow < 2:
                rainbow_cycle(0.02, j)
                if j == 255:
                    j = 0
                    rainbow +=1
                else:
                    j += 1
            
            if rainbow == 2:
                clear()
                snake(a)
                a+=1
                if a == 122:
                    snake(b)
                    b += 1
                    if b == 565:
                        snake(c)
                        c -= 1
                        if c == 318:
                            snake(d)
                            d += 1
                            if d == 671:
                                snake(e)
                                e += 1
                                if e == 152:
                                    snake(f)
                                    f += 1
                                    if f == 777:
                                        snake(g)
                                        g -= 1
                                        if g == 274:
                                            snake(h)
                                            h -= 1
                                            if h == 168:
                                                a = 0
                                                b = 457
                                                c = 318
                                                d = 566
                                                e = 137
                                                f = 672
                                                g = 289
                                                h = 274
                                                rainbow = 0



def function_call(location):
    # Andrew, this is where your stuff should go
    clear()
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