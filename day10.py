import numpy as np
import math
from collections import Counter, defaultdict
from functools import reduce, cache
from itertools import accumulate
from math import lcm
import re

pipeMap = {
    ('|', (1,0)) : (1,0),
    ('|', (-1,0)) : (-1,0),
    ('-', (0,1)) : (0,1),
    ('-', (0,-1)) : (0,-1),
    ('L', (1,0)) : (0,1),
    ('L', (0,-1)) : (-1,0),
    ('J', (1,0)) : (0,-1),
    ('J', (0,1)) : (-1,0),
    ('7', (-1,0)) : (0,-1),
    ('7', (0,1)) : (1,0),
    ('F', (-1,0)) : (0,1),
    ('F', (0,-1)) : (1,0),
    ('S', None) : (0,1)
}

def part1(lines):
    data = np.array([[c for c in line.strip()] for line in lines], dtype = str)
    path = getPath(data)
    return math.ceil(len(path)/2)

def part2(lines):
    print()
    data = np.array([[c for c in line.strip()] for line in lines], dtype = str)
    path = getPath(data)
    inside = 0
    for y in range(len(data)):
        print('... ' + str(y))
        for x in range(len(data[0])):
            if (y,x) not in path:
                crossings = 0
                for i in range(min(y,x) + 1):
                    if (y-i,x-i) in path and data[(y-i,x-i)] in ('|','-','F','J','S'):
                        crossings = crossings + 1
                inside = inside + (crossings % 2)
    return inside

def getPath(data):
    start = list(zip(*np.where(data == 'S')))[0]
    path = [start]
    curr = start
    move = pipeMap[data[curr], None]
    curr = tuple(prev + move for prev,move in zip(curr,move))

    while curr != start:
        path.append(curr)
        move = pipeMap[data[curr], move]
        curr = tuple(prev + move for prev,move in zip(curr,move))
    
    return path

if __name__ == "__main__":
    file = open("in.txt")
    # file = open("test.txt") 
    lines = file.readlines() 
    print(part1(lines))      
    print(part2(lines))
    file.close()