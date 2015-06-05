#!/usr/bin/env python3
# This script will try to solve the problem described in:
# https://www.hackerrank.com/challenges/tutorial-intro

if __name__ == "__main__":
    number_to_find = int(input())
    array_size = int(input())
    input_array = list(map(int, list(input().split())))
    print(input_array.index(number_to_find))