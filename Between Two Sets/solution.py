#!/bin/python3

import os
import sys

#
# Complete the getTotalX function below.
#

def getTotalX(a, b):
    total = 0
    for x in list(range(a[-1], b[0] + 1)):
        hold = 0
        for v in a:
            if (x % v == 0): hold += 1
            else: hold = 0; break    
        
        for c in b:
            if (c % x == 0): hold += 1
            else: hold = 0; break       
        if (hold == len(a) + len(b)):
            total += 1   
    return total

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    f.write(str(total) + '\n')

    f.close()
