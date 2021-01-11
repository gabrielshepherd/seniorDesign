import requests

response = requests.get('http://localhost:5000/light_on', json={'color': 'dumb', 'location': 'the moon'})
print(response.status_code)
print(response.text)