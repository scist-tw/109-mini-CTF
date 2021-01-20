#!/usr/bin/python3
from random import SystemRandom
from gmpy2 import isqrt, c_div , invert
from Crypto.Util.number import getPrime , bytes_to_long

urandom = SystemRandom()

def create_keypair(size):
    while True:
        p = getPrime(size // 2)
        q = getPrime(size // 2)
        if q < p < 2 * q:
            break

    n = p * q
    phi = (p - 1) * (q - 1)

    max_d = c_div(isqrt(isqrt(n)) , 3)
    max_d_bits = max_d.bit_length() - 1

    while True:
        d = urandom.getrandbits(max_d_bits)
        try:
            e = int(invert(d, phi))
            if (e * d) % phi == 1:
                break
        except:
            continue

    return  n , e , d , p , q

n , e , d , p , q = create_keypair(1024)

from secret import flag

m = bytes_to_long(flag)
c = pow(m , e , n)

a = """n = {}
e = {}
c = {}""".format(n , e , c)

with open("output.py" , "w") as f:
    f.write(a)
