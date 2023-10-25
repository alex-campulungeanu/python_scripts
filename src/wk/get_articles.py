from wsgiref import headers
import requests
import json
import time

url = '<base>intApp/articlelistviewbytype'

head={'Authorization': ''}

with open('articles.txt', 'a') as file:
    for i in range(10):
        payload = {
            "search_key": "",
            "emailID": "",
            "filter_parameters": {
                "article_type_list": [
                    "script"
                ],
                "service_line_list": [],
                "service_name_list": [],
                "entity_list": [],
                "technology_list": [],
                "file_type_list": [],
                "center_list": []
            },
            "pageNo": i+10,
            "displayRecords": 12,
            "sortBy": "views"
        }
        dt = json.dumps(payload)


        res = requests.post(url=url, data=dt, headers=head)

        json_res = res.json()
        records = json_res['records']
        # print(records)
        for record in records:
            print(record['articleId'])
            id = record['articleId']
            file.write(f"{id}\n")