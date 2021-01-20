#!/usr/bin/python3

from Crypto.Util.number import long_to_bytes

f = list(map(int , open("output" , "r").read().strip().split("\n")))

bit_ls = [0 , 1] * len(f)
res = ""

for i in range(len(f)):
    res = str(bit_ls[i] ^ (f[i] & 1)) + res

res = int(res , 2)

flag = long_to_bytes(res)
print(flag.decode())

