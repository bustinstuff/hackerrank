#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    left_diag_total = 0
    right_diag_total = 0

    arr_len = len(arr[0])

    left_diag_pos = 0
    right_diag_pos = arr_len
    for i in range(arr_len):
        left_diag_total += arr[i][left_diag_pos]
        right_diag_total += arr[i][right_diag_pos - 1]

        left_diag_pos += 1
        right_diag_pos -= 1

    return abs(left_diag_total - right_diag_total)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
