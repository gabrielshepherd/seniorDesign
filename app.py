from flask import Flask, request
app = Flask(__name__)

def function_call(location):
    # Andrew, this is where your stuff should go
    print(location)
    return

# if __name__=="__main__":
@app.route('/')
def connect():
    return "connection established"

# @app.route('/transmit')
# def receive_data():
#     location = request.json['location']
#     color = request.json['color']
#     print(location)
#     print(color)
#     return "data received"

@app.route('/transmit')
def receive_data():
    location = request.json['location']
    function_call(location)
    return "data received"