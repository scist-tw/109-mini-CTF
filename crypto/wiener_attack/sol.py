#!/usr/bin/python3
from owiener import attack
from wiener_attack import *
from output import *
from Crypto.Util.number import long_to_bytes

d = attack(e , n)
#d = wiener(e , n)

print(long_to_bytes(pow(c , d , n)).decode("latin-1"))
