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
        print(*arr)
        n -= 1

    if n == 0:
        n += 1

    arr[n-1] = value
    print(*arr)


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
