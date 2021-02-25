from flask import Flask, request, after_this_request
import threading
import time

def my_threaded_thing():
    t = threading.current_thread()
    count = 0
    while getattr(t, "do_run", True):
        print(count)
        count += 1
        time.sleep(1)
    print("ok im ded now")

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
    @after_this_request
    def after_this_request_func(response):
        print("after request")
        return response
    location = request.json['location']
    function_call(location)

    my_thread = threading.Thread(target=my_threaded_thing)
    my_thread.start()

    return "data received"

@app.before_request
def before_request_func():
    msg = "before request"
    print(msg)
    return msg

# @app.after_request
# @app.teardown_request
# def after_request_func():
#     msg = "after request"
#     print(msg)
#     return msg

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')