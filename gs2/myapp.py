"""
This is a simple application buit for testing the API
"""
import requests
import json
URL = "http://127.0.0.1:8000/stucreate/"
data = {
    'name': 'Sonam3',
    'roll': 102,
    'city': 'Ranchi3'
}
json_data = json.dumps(data)
r = requests.post(url = URL, data = json_data)
data = r.json()
print(data)
