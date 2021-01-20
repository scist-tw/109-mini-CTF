#!/usr/bin/python
from collections import Counter

c = open("output.txt" , "r").read().decode("hex")
#freq - sorted(set(text) , key = text.count)[::-1]

cnt = sorted(Counter(c).items() , key = lambda i : i[1] , reverse = True)
cnt = map(lambda i : i[0] , cnt)

freq = " EATNISORHLDCGWUFBYKPMVXJZQ"

mapping = {}

for i , t in enumerate(cnt):
    if i < 27:
        mapping[t] = freq[i]

res = ""

for i in c:
    if i in mapping.keys():
        res += mapping[i]

print(res)

