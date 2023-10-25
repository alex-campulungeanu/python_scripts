from wsgiref import headers
import requests
import json
import time

url = '<base>intApp/ratearticle/'

head={'Authorization': ''}

with open("articles.txt") as file:
    lines = file.read().splitlines()
    i = 0
    for line in lines:
        i += 1
        if line == 10:
            break
        print(line)
        payload = {
            "article_id": line,
            "user_id": "",
            "rating": 4
        }
        
        dt = json.dumps(payload)
        
        res = requests.post(url=url, data=dt, headers=head)

        json_res = res.json()
        print(json_res)