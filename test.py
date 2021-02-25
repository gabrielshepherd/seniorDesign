from flask import Flask
from multiprocessing import Process
import time

app = Flask(__name__)

def detachedProcessFunction(wait_time):
    i=0
    while i<wait_time:
        i = i+1
        print ("loop running %d" % i)
        time.sleep(1)

@app.route('/start')
def start():
    global p
    p = Process(target=detachedProcessFunction, args=(15))
    p.start()
    return render_template('layout.html')

if __name__ == '__main__':
    app.run(debug=True)