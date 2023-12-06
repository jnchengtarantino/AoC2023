import numpy as np
from collections import Counter, defaultdict
from functools import reduce, cache
from itertools import accumulate
from math import lcm, sqrt, ceil
import re

def part1(lines):
    races = getRaces(lines)
    chargeTimes = [solve(*race) for race in races]
    solutions = [ceil(maxTime) - (ceil(minTime) if ceil(minTime) != minTime else ceil(minTime) + 1) for minTime, maxTime in chargeTimes]
    return reduce(lambda x, y: x*y, solutions)

def part2(lines):
    race = getRaces([re.sub("\s+","",line) for line in lines])
    minTime, maxTime = solve(*race[0])
    return ceil(maxTime) - (ceil(minTime) if ceil(minTime) != minTime else ceil(minTime) + 1)


def getRaces(lines):
    return list(zip([int(time) for time in re.findall("(\d+)",lines[0])], [int(dist) for dist in re.findall("(\d+)",lines[1])]))

def solve(maxTime, minDist):
    return ((maxTime - sqrt(maxTime**2 - (4*minDist)))/2, (maxTime + sqrt(maxTime**2 - (4*minDist)))/2)

if __name__ == "__main__":
    file = open("in.txt")
    # file = open("test.txt") 
    lines = file.readlines() 
    print(part1(lines))      
    print(part2(lines))
    file.close()