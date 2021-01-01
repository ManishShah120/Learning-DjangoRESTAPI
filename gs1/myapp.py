"""
This Portion of code is not related to any django or django rest api framework. It is only created to test the API

"""

import requests

URL = "http://127.0.0.1:8000/students/"

r = requests.get(url=URL)

data = r.json()

print(data)
