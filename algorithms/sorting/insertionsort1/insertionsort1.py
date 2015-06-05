#!/usr/bin/env python3
# This script will try to solve the problem described in:
# https://www.hackerrank.com/challenges/insertionsort1


def sort_right(input_array):
    """
    This function will take the element to sort and will try to put it in the
    correct position
    """
    right_element = input_array[-1]
    for i in range(len(input_array)):
        if input_array[-(i+1)] >= right_element:
            if i+1 == len(input_array):
                input_array[-(i+1)] = right_element
            else:
                if input_array[-(i+2)] > right_element:
                    input_array[-(i+1)] = input_array[-(i+2)]
                else:
                    input_array[-(i+1)] = right_element
            print(" ".join(list(map(str, input_array))))

if __name__ == "__main__":
    array_size = int(input())
    input_array = list(map(int, list(input().split())))
    sort_right(input_array)