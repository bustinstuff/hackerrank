#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):

    largest_val = 0
    sum_largest_val = 0
    for i in range(len(ar)):
        val = int(ar[i])

        if val > largest_val:
            largest_val = val
            sum_largest_val = 1

        elif val == largest_val:
            sum_largest_val += 1

    return sum_largest_val

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
