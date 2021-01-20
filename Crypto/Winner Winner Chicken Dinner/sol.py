#!/usr/bin/python3

from owiener import attack
from output import n , e , c
from Crypto.Util.number import long_to_bytes

d = attack(e , n)

m = pow(c , d , n)
print(long_to_bytes(m).decode())

