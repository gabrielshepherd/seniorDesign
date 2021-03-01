import requests

def data_transmit(location):        # location is a string
    print("we are here")
    # response = requests.get('http://172.16.0.1:5000/transmit', json={'location': str(location)})
    response = requests.get('http://localhost:5000/transmit', json={'location': str(location)})
    print(response.status_code)
    print(response.text)
    return "data sent"
