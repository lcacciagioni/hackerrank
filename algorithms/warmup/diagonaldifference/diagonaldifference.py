#!/usr/bin/env python3
# This script will try to solve the problem described in:
# https://www.hackerrank.com/challenges/diagonal-difference

def diag_diff(matrix, size):
    sum_first_diag = 0
    sum_second_diag = 0
    for i in range(size):
        for j in range(size):
            if i == j:
                sum_first_diag += int(matrix[i][j])
                sum_second_diag += int(matrix[i][-(j+1)])

    result = abs(sum_first_diag - sum_second_diag)
    return result

if __name__ == '__main__':
    N = int(input())
    input_matrix = list()
    for _ in range(N):
        input_matrix.append(list(input().split()))

    print(diag_diff(input_matrix, N))