#!/usr/bin/env python3
# This script will try to solve the problem described in:
# https://www.hackerrank.com/challenges/service-lane


def get_vehicle(lane, start, end):
    """
    This function will detect which vehicle can pass all the way from the
    begining to the exit.
    """
    return min(lane[start:end])

if __name__ == "__main__":
    n, t = input().split()
    lanes = input().split()
    test_cases = list()
    for i in range(int(t)):
        test_cases.append(input().split())

    for i in range(int(t)):
        st = int(test_cases[i][0])
        en = int(test_cases[i][1]) + 1
        print(get_vehicle(lanes, st, en))