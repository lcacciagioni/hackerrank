#!/usr/bin/env python3
# This script will try to solve the problem described in:
# https://www.hackerrank.com/challenges/chocolate-feast
# CAUTION I HAVE 18 OVER 20 POINTS


def num_choc(n, c, m):
    """
    This function will evaluate the real amount of chocolate to be eated by
    this guy.
    n --> Money
    c --> Cost of chocolate
    m --> # of wrappers to get one more
    """
    n = int(n)
    c = int(c)
    m = int(m)
    choc_count = (n // c) + (n // c // m) + (
        (((n // c) % m) + (n // c // m)) // m)
    return choc_count

if __name__ == '__main__':
    T = int(input())
    inputs = list()
    for _ in range(T):
        inputs.append(input().split())

    for i in range(T):
        print(num_choc(inputs[i][0],inputs[i][1],inputs[i][2]))