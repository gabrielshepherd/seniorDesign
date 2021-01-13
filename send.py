import requests

def data_transmit(location):        # location is a string
    print("we are here")
    response = requests.get('http://192.168.0.60:5000/transmit', json={'location': str(location)})
    print(response.status_code)
    print(response.text)
    return "data sent"