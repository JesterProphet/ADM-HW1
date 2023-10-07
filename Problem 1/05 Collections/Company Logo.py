#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':

    s = input()
    dict = {}

    for char in set(s):
        dict[char] = s.count(char)

    sorted_dict = {val[0]: val[1] for val in sorted(dict.items(), key=lambda item: (-item[1], item[0]))}

    for i in range(0, 3):
        print(list(sorted_dict)[i] + " " + str(sorted_dict[list(sorted_dict)[i]]))




