#!/usr/bin/env python3
# This script will try to solve the problem described in:
# https://www.hackerrank.com/challenges/halloween-party


def get_max_combination(total_cuts):
    """
    This function will try to get the major number of pieces
    """
    max_pieces = 0
    for i in range(total_cuts):
        result = i * (total_cuts - i)
        if result > max_pieces:
            max_pieces = result
    print(max_pieces)

if __name__ == "__main__":
    t = int(input())
    inputs = list()
    for i in range(t):
        inputs.append(int(input()))

    for i in range(t):
        get_max_combination(inputs[i])