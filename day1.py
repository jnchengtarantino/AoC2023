import numpy as np
from collections import Counter, defaultdict
from functools import reduce, cache
from itertools import accumulate
from math import lcm
import re

# file = open("testinput.txt")
file = open("day1input.txt")
ans = []
nums = {"1","2","3","4","5","6","7","8","9","0"}
texts = {"one","two","three","four","five","six","seven","eight","nine","zero"}

# part 1
# lines = file.readlines()
# for line in lines:
#     digits = re.findall("\d", line)
#     ans.append(int(digits[0] + digits[-1]))
# print(sum(ans))

# part 2
lines = file.readlines()
for line in lines:
    line = line.replace("one","one1one").replace("two","two2two").replace("three","three3three").replace("four","four4four").replace("five","five5five").replace("six","six6six").replace("seven","seven7seven").replace("eight","eight8eight").replace("nine", "nine9nine").replace("zero","zero0zero")
    digits = re.findall("\d", line)
    ans.append(int(digits[0] + digits[-1]))
print(sum(ans))
        
file.close()