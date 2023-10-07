#!/bin/python3

import math
import os
import random
import re
import sys


def superDigit(n, k):

    digit = map(int, n)

    return result(str(sum(digit))*k)


def result(digit):

    if len(digit) == 1:
        return digit[0]
    else:
        digit = map(int, digit)
        return result(str(sum(digit)))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
