import numpy as np
from collections import Counter, defaultdict
from functools import reduce, cache
from itertools import accumulate
from math import lcm
import re

def part1(lines):
    data = parseIn(lines)
    results = []
    for line in data:
        levels = [line]
        while not all([x == 0 for x in levels[-1]]):
            levels.append([levels[-1][i+1] - levels[-1][i] for i in range(len(levels[-1])-1)])
        results.append(sum([level[-1] for level in levels]))
    return sum(results)

def part2(lines):
    data = parseIn(lines)
    results = []
    for line in data:
        levels = [line]
        while not all([x == 0 for x in levels[-1]]):
            levels.append([levels[-1][i+1] - levels[-1][i] for i in range(len(levels[-1])-1)])
        results.append(sum([level[0]*((-1)**i) for i,level in enumerate(levels)]))
    return sum(results)

def parseIn(lines):
    return [[int(x) for x in re.findall("(-?\d+)",line)] for line in lines]
    
if __name__ == "__main__":
    file = open("in.txt")
    # file = open("test.txt") 
    lines = file.readlines() 
    print(part1(lines))      
    print(part2(lines))
    file.close()