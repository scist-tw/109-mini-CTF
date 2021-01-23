#!/usr/bin/python3

from PIL import Image
from numpy import *

data = open("output" , "r").read().strip()
h = 88
w = len(data) // h

new = Image.new(mode="L" , size=(w , h))
new = array(new)

for x in range(h):
    for y in range(w):
        if data[x * w + y] == "0":
            new[x][y] = 255
        else:
            new[x][y] = 1

res = Image.fromarray(new)
res.save("flag.png")

