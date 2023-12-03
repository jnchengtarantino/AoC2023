import numpy as np
from collections import Counter, defaultdict
from functools import reduce, cache
from itertools import accumulate
from math import lcm
import re

# file = open("in.txt")
file = open("test.txt")

lines = file.readlines()
# symbols = set()
potentialGears = {}

for i,line in enumerate(lines):
    for j,c in enumerate(line.strip()):
        # if c not in '1234567890.': symbols.add((i,j))
        if c == '*': potentialGears[(i,j)] = []

parts = []
for i,line in enumerate(lines):
    for m in re.finditer('(\d+)', line):
        area = {(x,y) for y in range(m.start()-1, m.end()+1) for x in (i-1,i,i+1)}
        # if area & symbols: parts.append(int(m.group()))
        for adj in area & potentialGears.keys(): potentialGears[adj].append(int(m.group()))

# print(sum(parts))
print(sum( [v[0]*v[1] for v in potentialGears.values() if len(v)==2] )) 
file.close()