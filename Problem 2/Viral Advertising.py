#!/bin/python3

import math
import os
import random
import re
import sys


def viralAdvertising(n):

    shared = 5
    likes = 0

    for i in range(0, n):
        shared = shared // 2
        likes += shared
        shared = shared * 3

    return likes


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
