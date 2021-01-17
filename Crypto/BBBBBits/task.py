#!/usr/bin/python
from os import urandom
from secret import flag
from Crypto.Util.number import bytes_to_long , getPrime
from random import randint
from PIL import Image
from math import log
from gmpy2 import get_exp
from operator import mul
from sympy.ntheory.residue_ntheory import discrete_log

def bit_generate(length):
    status = 1
    ls = []

    for i in range(length):
        ls.append(abs(status - 1))
        status = abs(status - 1)

    return ls

def push(stack):
    while stack > 0:
        if stack & 1:
            break
        else:
            stack >>= 1
    return stack

def calc(bits , m , i , l):
    res  = push(m << (get_exp(1 << (2 * l)))) & (0 | m // (pow(2 , i)))
    res |= getPrime(300) << 3
    res ^= (bits << 5) 
    return res

key = bytes_to_long(urandom(8))
p , q , r = [getPrime(100) for _ in range(3)]
n = pow(2 , randint(pow(1 , 1) , 1 << randint(2 , 10)))
n = (lambda a , b , c , d : a * b * c * d)(p , q , r , n)
e = getPrime(5)

flag = bytes_to_long(flag)
bit_ls = bit_generate(flag.bit_length())

with open("output" , "w") as f:
    for i in range(flag.bit_length()):
        res = calc(bit_ls[i] , flag , i , flag.bit_length())
        res = pow(res ^ bit_ls[i] , e , n)
        f.write(str(res) + "\n")

