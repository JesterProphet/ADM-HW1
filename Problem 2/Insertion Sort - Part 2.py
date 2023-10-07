#!/bin/python3

import math
import os
import random
import re
import sys

def insertionSort1(n, arr):

    value = arr[n-1]

    while value < arr[n-2] and n > 1:
        arr[n-1] = arr[n-2]
        n -= 1

    if n == 0:
        n += 1

    arr[n-1] = value

    return arr


def insertionSort2(n, arr):

    for i in range(2, n+1):
        arr = insertionSort1(len(arr[:i]), arr[:i]) + arr[i:]
        print(*arr)


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
