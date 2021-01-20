#!/usr/bin/sage

from sage.all import *
from output import e , n , c
from Crypto.Util.number import long_to_bytes

lst = continued_fraction(Integer(e) / Integer(n))
conv = lst.convergents()

for i in conv:
    d = int(i.denominator())
    try:
        m = long_to_bytes(pow(c , d , n))
        if b"SCIST" in m:
            print(m.decode())
            break
    except:
        continue


