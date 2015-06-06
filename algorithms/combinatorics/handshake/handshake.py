#!/usr/bin/env python3
# This script will try to solve the problem described in:
# https://www.hackerrank.com/challenges/handshake
from math import factorial


def get_handshake(people):
    if people == 1:
        combinations = 0
    else:
        combinations = factorial(people)/((
            factorial(2)) * (factorial(people-2)))
    return int(combinations)

if __name__ == '__main__':
    T = int(input())
    peoples = list()
    for _ in range(T):
        peoples.append(int(input()))

    for i in range(T):
        print(get_handshake(peoples[i]))