#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    pos_tot = 0
    neg_tot = 0
    zer_tot = 0

    arr_len = 0
    for i in arr:

        if i > 0:
            pos_tot += 1

        elif i < 0:
            neg_tot += 1

        else:
            zer_tot += 1

        arr_len += 1

    print(round(pos_tot / arr_len, 6))
    print(round(neg_tot / arr_len, 6))
    print(round(zer_tot / arr_len, 6))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
