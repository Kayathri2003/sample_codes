#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    Z_C=0
    M_C=0
    P_C=0
    for i in arr:
        if i==0:
            Z_C+=1
        elif str(i).startswith("-"):
            M_C+=1
        else:
            P_C+=1
    print(P_C,Z_C,M_C)
    # p=P_C/len(arr)
    # m=M_C/len(arr)
    # z=Z_C/len(arr)
    # print(f'{p:.6f} \n {m:.6f} \n {z:.6f}')

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
