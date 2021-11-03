#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def UCLN(a, b):
    if b == 0:
        return a
    elif a % b == 0:
        return b
    else:
        return UCLN(b, a%b)

def getTotalX(a, b):
    # Write your code here
    BCNN = 1
    a.sort()
    b.sort()
    if len(a) == 1:
        BCNN = a[0]
    elif len(a) >= 2:
        BCNN = a[0] * a[1] / UCLN(a[0], a[1])
        for i in range(2, len(a)):
            BCNN = a[i] * BCNN / UCLN(a[i], BCNN)
    result = [BCNN * i for i in range(b[0] / BCNN + 1) if BCNN * i <= b[0] and BCNN * i > a[-1]]
    
    return len(result)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    print(total)

    # fptr.write(str(total) + '\n')

    # fptr.close()
