#!/usr/bin/env python3
# This script will try to solve the problem described in:
# https://www.hackerrank.com/challenges/fibonacci-modified


def mod_fib(first_term, second_term, limit, step):
    step += 1
    new_term = second_term * second_term + first_term
    if limit == step:
        print(new_term)
    else:
        mod_fib(second_term, new_term, limit, step)


if __name__ == "__main__":
    ft, st, lim = input().split()
    mod_fib(int(ft), int(st), int(lim), 2)