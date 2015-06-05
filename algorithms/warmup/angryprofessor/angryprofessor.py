#!/usr/bin/env python3
# This script will try to solve the problem described in:
# https://www.hackerrank.com/challenges/angry-professor


def test_give_class():
    """
    This function will test if the proffesor gives the class or not
    """


if __name__ == "__main__":
    test_cases = int(input())
    inputs = list()
    for i in range(test_cases):
        n_k = input()
        arrives = input()
        inputs.append([n_k,arrives])