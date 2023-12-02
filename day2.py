import numpy as np
from collections import Counter, defaultdict
from functools import reduce, cache
from itertools import accumulate
from math import lcm
import re

file = open("in.txt")
# file = open("test.txt")

sum = 0

lines = file.readlines()
for i, line in enumerate(lines):
    blocks = {
        "r":0,
        "g":0,
        "b":0
    }

    maxes = re.findall("(\d+) (\w)", line.strip())
    for n, color in maxes:
           blocks[color] = max(blocks[color], int(n))

    # if blocks["r"]<=12 and blocks["g"]<=13 and blocks["b"]<=14:
    #     sum += i+1  

    sum += blocks["b"]*blocks["r"]*blocks["g"] 

print(sum)
file.close()