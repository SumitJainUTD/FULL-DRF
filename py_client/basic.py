import requests

import datetime
from time import sleep


def get_random_string(prefix="sample"):
    sleep(1)
    return prefix + "_" + str(datetime.datetime.now()) \
        .replace("-", "") \
        .replace(" ", "") \
        .replace(":", "").split(".")[0]


endpoint = "http://127.0.0.1:3000/api/"

title = get_random_string("title")
content = get_random_string("content")
post_response = requests.post(endpoint, json={'titlee': title, 'content': content})
print((post_response.json()))

get_response = requests.get(endpoint, params={'abc': 123}, json={'query': 'hello world'})
print(get_response.json())
