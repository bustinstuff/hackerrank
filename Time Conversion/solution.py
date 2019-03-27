#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    out = s[2:-2]

    if s[-2:] == 'AM' and s[0:2] == '12':
        out = '00' + out

    elif s[-2:] == 'PM' and s[0:2] != '12':
        out = str(12 + int(s[0:2])) + out

    else:
        out = s[0:2] + out

    return out

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
