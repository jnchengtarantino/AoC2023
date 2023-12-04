import numpy as np
from collections import Counter, defaultdict
from functools import reduce, cache
from itertools import accumulate
from math import lcm
import re

def part1(lines):
    points = 0
    for line in lines:
        _, card = line.strip().split(':')
        winning, nums = card.split('|')
        winning = {int(w) for w in re.findall('(\d+)', winning)}
        nums = {int(n) for n in re.findall('(\d+)', nums)}
        points += 2**(len(winning & nums)-1) if len(winning & nums) > 0 else 0
    return points
        

def part2(lines):
    dp = [1] * len(lines)
    matches = []
    for line in lines:
        _, card = line.strip().split(':')
        winning, nums = card.split('|')
        winning = {int(w) for w in re.findall('(\d+)', winning)}
        nums = {int(n) for n in re.findall('(\d+)', nums)}
        matches.append(len(winning & nums))
    
    for i in range(len(matches)):
        for j in range(i+1, i+matches[i]+1):
            dp[j] += dp[i]
    
    return sum(dp)
    
if __name__ == "__main__":
    file = open("in.txt")
    # file = open("test.txt")  
    lines = file.readlines()
    print(part1(lines))      
    print(part2(lines))
    file.close()