#!/usr/bin/env python3
# This script will try to solve the problem described in:
# https://www.hackerrank.com/challenges/lonely-integer

def lonelyinteger(b):
    """
    This function will do the job
    """
    num_list = list(b)
    for num in num_list:
        """
        Si el conteo de ocurrencias es uno lo devolvemos
        """
        if num_list.count(num) == 1:
            return num

if __name__ == '__main__':
    a = int(input())
    b = map(int, input().strip().split(" "))
    print(lonelyinteger(b))
