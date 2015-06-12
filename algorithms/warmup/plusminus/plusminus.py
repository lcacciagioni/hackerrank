#!/usr/bin/env python3
# This script will try to solve the problem described in:
# https://www.hackerrank.com/challenges/plus-minus


def plusminus(input_array, size):
    positive_count = 0
    negative_count = 0
    zeroes_count = 0
    for i in range(size):
        if int(input_array[i]) < 0:
            negative_count += 1
        elif int(input_array[i]) > 0:
            positive_count += 1
        else:
            zeroes_count += 1

    positive_count = positive_count / size
    negative_count = negative_count / size
    zeroes_count = zeroes_count / size

    return (positive_count, negative_count, zeroes_count)

if __name__ == "__main__":
    N = int(input())
    input_array = input().split()
    print("%.3f\n%.3f\n%.3f\n" % plusminus(input_array, N))