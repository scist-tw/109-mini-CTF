#!/usr/bin/python
from collections import Counter

f = open("output.txt" , "r")
c = f.readline().strip().decode("hex")

cnt = sorted(Counter(c).items() , key = lambda i : i[1] , reverse = True)
cnt = map(lambda i : i[0] , cnt)

freq = f.readline()

mapping = {}

for i , t in enumerate(cnt):
    if i < 27:
        mapping[t] = freq[i]

res = ""

for i in c:
    if i in mapping.keys():
        res += mapping[i]

print(res)

