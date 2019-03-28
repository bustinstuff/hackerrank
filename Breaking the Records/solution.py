#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):

    recordBreaks = [0,0]

    high = scores[0]
    low = scores[0]
    for score in scores:
        if score > high:
            recordBreaks[0] += 1
            high = score
        elif score < low:
            recordBreaks[1] += 1
            low = score
    
    return(recordBreaks)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
