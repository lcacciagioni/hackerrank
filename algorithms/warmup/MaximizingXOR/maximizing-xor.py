#!/usr/bin/env python3
# Problem: https://www.hackerrank.com/challenges/maximizing-xor
from itertools import *

def maxXor(l, r, max_xor):
    for i in combinations_with_replacement(range(l,r+1),2):
       c = i[0]^i[1]
       if c > max_xor:
           max_xor = c
    return max_xor

if __name__ == '__main__':
    l = int(input())
    r = int(input())
    print(maxXor(l, r, 0))
