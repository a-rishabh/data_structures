#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    min = arr[0]
    for elem in arr:
        if elem < min:
            min = elem
            
    max = arr[-1]
    for elem in arr:
        if elem > max:
            max = elem
            
    arr.remove(max)
    min_t = 0
    max_t = 0
    for elem in arr:
        min_t += elem
        
    arr.append(max)
    arr.remove(min)

    for elem in arr:
        max_t += elem
        
    print(min_t, max_t)
    # print(max_t)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
