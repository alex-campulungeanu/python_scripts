from wsgiref import headers
import requests
import json
import time

url = 'intApp/getarticledetailsbyid'

head={'Authorization': ''}

with open("articles.txt") as file:
    lines = file.read().splitlines()
    i = 0
    for line in lines:
        # i += 1
        # if line == 10:
        #     break
        print(line)
        payload = {
            "emailID":"",
            "articleId": line
        }
        
        dt = json.dumps(payload)
        
        res = requests.post(url=url, data=dt, headers=head)

        # print(res.content)
        json_res = res.json()
        # print(json_res)