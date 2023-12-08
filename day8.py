import numpy as np
from collections import Counter, defaultdict
from functools import reduce, cache
from itertools import accumulate
from math import lcm
import re

def part1(lines):
    directions = lines[0].strip()
    graph = parseGraph(lines[2:])
    i = 0
    curr = 'AAA'
    while curr != 'ZZZ':
        dir = directions[i%len(directions)]
        curr = graph[curr][0] if dir == 'L' else graph[curr][1]
        i = i+1
    return i

def part2(lines):
    directions = lines[0].strip()
    graph = parseGraph(lines[2:])
    starting = [key for key in graph.keys() if key[-1]=='A']
    results = []

    for s in starting:
        i = 0
        curr = s
        while curr[-1] != 'Z':
            dir = directions[i%len(directions)]
            curr = graph[curr][0] if dir == 'L' else graph[curr][1]
            i = i+1
        results.append(i)

    return lcm(*results)

def parseGraph(lines):
    return {k: (l,r) for k,l,r in (re.findall("([0-9A-Z]+)", line) for line in lines)}
    
if __name__ == "__main__":
    file = open("in.txt")
    # file = open("test.txt") 
    lines = file.readlines() 
    print(part1(lines))      
    print(part2(lines))
    file.close()