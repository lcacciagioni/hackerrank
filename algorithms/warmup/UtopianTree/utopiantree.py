#!/usr/bin/env python3
# Problem: https://www.hackerrank.com/challenges/utopian-tree

def utopiantree(n):
    tree_eight = 1
    for cycle in range(n):
        if (cycle % 2) == 0 and cycle != 0:
            tree_eight = tree_eight + 1
        if (cycle % 2) != 0 and cycle != 0:
            tree_eight = tree_eight * 2
    return tree_eight

if __name__ == '__main__':
    a = int(input())
    for test_case in range(a):
        cycles = int(input())
        print(utopiantree(cycles))
