#!/usr/bin/env python3
# This script will try to solve the problem described in:
# https://www.hackerrank.com/challenges/angry-professor

if __name__ == "__main__":
    test_cases = int(input())
    inputs = list()
    for i in range(test_cases):
        n_k = input()
        arrives = input()
        inputs.append([n_k, arrives])

    for j in range(test_cases):
        limit = int(inputs[j][0].split()[1])
        tot_students = int(inputs[j][0].split()[0])
        late_students = 0
        for k in range(tot_students):
            if int(inputs[j][1].split()[k]) > 0:
                late_students += 1
        if tot_students - late_students < limit:
            print("YES")
        else:
            print("NO")