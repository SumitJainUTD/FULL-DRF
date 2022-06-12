import requests

import datetime
from time import sleep

endpoint = "http://127.0.0.1:3000/api/products/2/"

get_response = requests.get(endpoint)
print(get_response.json())
