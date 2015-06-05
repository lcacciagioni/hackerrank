#!/usr/bin/env python3
# This script will try to solve the problem described in:
# https://www.hackerrank.com/challenges/cut-the-sticks


def sticks_counter(stick_group, group_len):
    """
    Ok I'll try to do this recursive
    """
    if group_len > 0:
        cutted_sticks = 0
        minimun = min(list(map(int, stick_group)))
        new_stick_group = list()
        for i in range(group_len):
            if int(stick_group[i]) >= minimun:
                cutted_sticks += 1
                result = int(stick_group[i]) - minimun
                if result > 0:
                    new_stick_group.append(result)
        print(cutted_sticks)
        sticks_counter(new_stick_group, len(new_stick_group))


if __name__ == "__main__":
    length = int(input())
    sticks = input().split()
    sticks_counter(sticks,length)