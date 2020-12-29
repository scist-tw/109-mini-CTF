#!/usr/bin/python3
from random import shuffle
from secret import flag
from string import ascii_uppercase as upper 

alpha = upper + " "
new_alpha = list(alpha)

shuffle(new_alpha)

new_alpha = "".join(new_alpha)

res = ""

for i in flag:
    res += new_alpha[alpha.index(i)]

res = res.encode().hex()

with open("output.txt" , "w") as f:
    f.write(res)
