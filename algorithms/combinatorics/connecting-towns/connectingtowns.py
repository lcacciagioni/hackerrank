#!/usr/bin/env python3
# This script will try to solve the problem described in:
# https://www.hackerrank.com/challenges/connecting-towns


def con_town(routes):



if __name__ == "__main__":
    T = int(input())
    towns_routes = list()
    for i in range(T):
        towns = input()
        routes = input()
        towns_routes.append([towns, routes])

    for i in range(T):
        con_town(towns_routes[i][1])