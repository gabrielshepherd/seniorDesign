# import requests

# response = requests.get('http://localhost:5000/light_on', json={'color': 'dumb', 'location': 'the moon'})
# response = requests.get('http://192.168.0.60:5000/transmit', json={'color': 'dumb', 'location': 'the moon'})
# print(response.status_code)
# print(response.text)

# import importlib
# importlib.import_module("send", package="data_transmit")
# return_string = data_transmit("Zero Spouse Mouse House")

from send import *
import requests
return_string = data_transmit("Zero Spouse Mouse House")
print(return_string)