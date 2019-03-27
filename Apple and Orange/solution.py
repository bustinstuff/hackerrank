#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    house_apples = 0
    house_oranges = 0

    for i in range(len(apples)):
        this_len = (a + apples[i])
        if this_len >= s and this_len <= t:
            house_apples += 1

    for i in range(len(oranges)):
        this_len = (b + oranges[i])
        if this_len <= t and this_len >= s:
            house_oranges += 1

    print(house_apples)
    print(house_oranges)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
