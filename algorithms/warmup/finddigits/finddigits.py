#!/usr/bin/env python3
# This script will try to solve the problem described in:
# https://www.hackerrank.com/challenges/find-digits


def find_div(num):
    """
    This function will find and count the digits that divide itself with 0 as
    module
    """
    list_numbers = [int(d) for d in str(num)]
    num_sum = 0
    for i in list_numbers:
        if i != 0 and (int(num) % i) == 0:
            num_sum += 1
    return num_sum

if __name__ == '__main__':
    T = int(input())
    numbers = list()
    for _ in range(T):
        numbers.append(int(input()))

    for j in range(T):
        print(find_div(numbers[j]))