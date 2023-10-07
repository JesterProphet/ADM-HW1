#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):

    for sub_string in s[:].split():
        s = s.replace(sub_string, sub_string.capitalize())

    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
