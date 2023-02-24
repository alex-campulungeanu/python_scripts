import requests

# url = 'https://mihaivasilescublog.ro/wp-content/plugins/comment-rating//ck-processkarma.php'
# url = 'https://arhiblog.ro/wp-admin/admin-ajax.php'
url = 'https://zoso.ro/wp-content/plugins/comment-rating//ck-processkarma.php'

form_data = {
    'id': '1874793',
    'action': 'add',
    'path': 'https://zoso.ro/wp-content/plugins/comment-rating/',
    'imgIndex': '1_14_',
    'nonce': 'e341bde08b'
}

# form_data = {
#     'comment_id': '1900282',
#     'action': 'cld_comment_ajax_action',
#     'type': 'like',
#     '_wpnonce': '3d8fefb57d',
# }

headers = {
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36","x-requested-with": "XMLHttpRequest,"
}

# headers = {
#     ":authority": "mihaivasilescublog.ro",
#     ":method": "POST",
#     ":path": "/wp-content/plugins/comment-rating//ck-processkarma.php",
#     ":scheme": "https",
#     "accept": "*/*",
#     "accept-encoding": "gzip, deflate, br",
#     "accept-language": "en-US,en;q=0.9",
#     "cache-control": "no-cache",
#     "content-length": "136",
#     "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
#     "origin": "https://mihaivasilescublog.ro",
#     "pragma": "no-cache",
#     "referer": "https://mihaivasilescublog.ro/2023/01/09/vreti-facem/",
#     "sec-ch-ua": """Not?A_Brand"";v=""8"", ""Chromium"";v=""108"", ""Google Chrome"";v=""108""",
#     "sec-ch-ua-mobile": "?0",
#     "sec-ch-ua-platform": """Windows""",
#     "sec-fetch-dest": "empty",
#     "sec-fetch-mode": "cors",
#     "sec-fetch-site": "same-origin",
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
#     "x-requested-with": "XMLHttpRequest,"
# }

server = requests.post(url, data=form_data, allow_redirects=False)

output = server.text

print('The response from the server is: \n', output)


""""
:authority: mihaivasilescublog.ro
:method: POST
:path: /wp-content/plugins/comment-rating//ck-processkarma.php
:scheme: https
accept: */*
accept-encoding: gzip, deflate, br
accept-language: en-US,en;q=0.9
cache-control: no-cache
content-length: 136
content-type: application/x-www-form-urlencoded; charset=UTF-8
origin: https://mihaivasilescublog.ro
pragma: no-cache
referer: https://mihaivasilescublog.ro/2023/01/09/vreti-facem/
sec-ch-ua: "Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
sec-fetch-dest: empty
sec-fetch-mode: cors
sec-fetch-site: same-origin
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36
x-requested-with: XMLHttpRequest
"""



# id: 1874793
# action: add
# path: https%3A%2F%2Fzoso.ro%2Fwp-content%2Fplugins%2Fcomment-rating%2F
# imgIndex: 1_14_
# nonce: e341bde08b