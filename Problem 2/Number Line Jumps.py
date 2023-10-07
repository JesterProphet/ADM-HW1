#!/bin/python3

import math
import os
import random
import re
import sys


def kangaroo(x1, v1, x2, v2):

    positions = [x1, x2]
    speeds = [v1, v2]

    diff_position = max(x1, x2) - min(x1, x2)
    diff_speed = max(v1, v2) - min(v1, v2)

    if positions.index(min(x1, x2)) == speeds.index(max(v1, v2)) and v1 != v2:
        if diff_speed <= diff_position and diff_position % diff_speed == 0:
            return "YES"
        else:
            return "NO"
    else:
        return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
