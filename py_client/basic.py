import requests

endpoint = "http://127.0.0.1:3000/api/"

get_response = requests.get(endpoint, params={'abc':123}, json={'query': 'hello world'})
print(get_response.json())