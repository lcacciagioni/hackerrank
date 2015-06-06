#!/usr/bin/env python3
# This script will try to solve the problem described in:
# https://www.hackerrank.com/challenges/minimum-draws


def min_draw(num_pairs):
    return num_pairs+1


if __name__ == "__main__":
    T = int(input())
    pairs = list()
    for i in range(T):
        pairs.append(int(input()))

    for i in range(T):
        print(min_draw(pairs[i]))