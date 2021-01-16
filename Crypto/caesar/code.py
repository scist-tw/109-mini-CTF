import base64
flag = open('flag', 'r').read()

move = 123
output = ''
for i in flag:
	nxt = chr((ord(i)+move)%128)
	output += nxt
with open('output.txt', 'w') as f:
	f.write(base64.b64encode(output.encode()).decode())

