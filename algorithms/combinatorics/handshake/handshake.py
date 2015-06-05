#!/usr/bin/env python3
# This script will try to solve the problem described in:
# https://www.hackerrank.com/challenges/handshake
from itertools import combinations


def get_handshake(people):
    return len(list(combinations(range(people), 2)))

if __name__ == '__main__':
    T = int(input())
    peoples = list()
    for _ in range(T):
        peoples.append(int(input()))

    for i in range(T):
        get_handshake(peoples[i])