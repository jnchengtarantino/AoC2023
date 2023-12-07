import numpy as np
from collections import Counter, defaultdict
from functools import reduce, cache
from itertools import accumulate
from math import lcm
import re

handOrder = ((1,1,1,1,1), (2,1,1,1), (2,2,1), (3,1,1), (3,2), (4,1), (5,))
cardOrder = ('2','3','4','5','6','7','8','9','T','J','Q','K','A')
cardOrder2 = ('J','2','3','4','5','6','7','8','9','T','Q','K','A')

def part1(lines):
    hands = parseHands(lines)
    hands.sort(key=handSort)
    return sum([(i+1)*hand[1] for i,hand in enumerate(hands)])

def part2(lines):
    hands = parseHands(lines)
    hands.sort(key=handSort2)
    return sum([(i+1)*hand[1] for i,hand in enumerate(hands)])

def parseHands(lines):
    return [(line[0],int(line[1])) for line in (line.split() for line in lines)]

def handSort(hand):
    cards, _ = hand
    counter = Counter(cards)
    key = list(counter.values())
    key.sort(reverse=True)
    keyTuple = tuple(key)
    return (handOrder.index(keyTuple), *[cardOrder.index(c) for c in cards])

def handSort2(hand):
    cards, _ = hand
    counter = Counter(cards)
    sortedCounter = counter.most_common()
    mostCommon = None
    for e in sortedCounter:
        if e[0] != 'J':
            mostCommon = e[0]
            break
    else:
        mostCommon = '2'

    counterReplaced = Counter(cards.replace('J',mostCommon))
    key = list(counterReplaced.values())
    key.sort(reverse=True)
    keyTuple = tuple(key)
    return (handOrder.index(keyTuple), *[cardOrder2.index(c) for c in cards])
        
    
if __name__ == "__main__":
    file = open("in.txt")
    # file = open("test.txt") 
    lines = file.readlines() 
    print(part1(lines))      
    print(part2(lines))
    file.close()