#!/usr/bin/python3
from random import shuffle
from secret import flag
from string import ascii_uppercase as upper 
from collections import Counter

alpha = upper + " "
new_alpha = list(alpha)

shuffle(new_alpha)

new_alpha = "".join(new_alpha)

res = ""

for i in flag:
    res += new_alpha[alpha.index(i)]

res = res.encode().hex()
freq = "".join(map(lambda i : i[0] , sorted(Counter(flag).items() , key = lambda i : i[1] , reverse = True)))

with open("output.txt" , "w") as f:
    f.write(f"{res}\n{freq}")
