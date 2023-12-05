import numpy as np
from collections import Counter, defaultdict
from functools import reduce, cache
from itertools import accumulate, groupby
from math import lcm
import re

def part1(lines):
    seeds = [int(x) for x in re.findall("(\d+)", lines[0])]
    mapList = getMapList([line for line in lines[2:] if line.strip() != ''])
    return min([mapTraverse(seed, mapList) for seed in seeds])

def part2(lines):
    seedRanges = [r.split() for r in re.findall("(\d+\s+\d+)", lines[0])]
    seedRanges = [(int(start), int(length)) for start, length in seedRanges]
    mapList = getInverseMapList([line for line in lines[2:] if line.strip() != ''])
    print(seedRanges)
    print(mapList)
    i = 1
    while True:
        testVal = mapTraverse(i,mapList)
        for start,length in seedRanges:
            if start<=testVal<start+length:
                return i
        if i%100000 == 0 : print(i)
        i = i+1

def getMapList(lines):
    return [parseMap(list(group)) for k, group in groupby(lines, lambda line: 'map' not in line) if k]
    
def parseMap(lines):
    m = {}
    for line in lines:
        destStart, sourceStart, rangeLen = [int(x) for x in line.split()]
        m[(sourceStart, rangeLen)] = destStart
    return m

def mapTraverse(seed, mapList):
    prev = seed
    for m in mapList:
        for k in m.keys():
            diff = prev - k[0]
            if 0 <= diff < k[1]:
                prev = m[k] + diff
                break
    return prev
    
def getInverseMapList(lines):
    return [parseInverseMap(list(group)) for k, group in groupby(lines, lambda line: 'map' not in line) if k][::-1]

def parseInverseMap(lines):
    m = {}
    for line in lines:
        destStart, sourceStart, rangeLen = [int(x) for x in line.split()]
        m[(destStart, rangeLen)] = sourceStart
    return m

if __name__ == "__main__":
    file = open("in.txt")
    # file = open("test.txt")
     
    lines = file.readlines() 
    print(part1(lines))      
    print(part2(lines))
    file.close()