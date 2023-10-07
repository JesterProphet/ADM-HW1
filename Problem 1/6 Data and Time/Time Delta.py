#!/bin/python3

import math
import os
import random
import re
import sys

from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):

    date1 = datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
    date2 = datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")

    date_diff = str(int(abs(date1 - date2).total_seconds()))

    return date_diff


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
