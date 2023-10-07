#!/bin/python3

import math
import os
import random
import re
import sys


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

concatenated_string = ""

for i in range(0, m):
    for string in matrix:
        concatenated_string = concatenated_string + string[i]

concatenated_string = re.sub(r"(?<=[a-zA-Z0-9])[ !@#$%&]+(?=[a-zA-Z0-9])", " ", concatenated_string)

print(concatenated_string)
