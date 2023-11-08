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
    plus = 0
    minus = 0
    
    plus = len([x for x in arr if x > 0])
    minus = len([x for x in arr if x < 0])
    # zero = len(arr) - plus - minus
    
    
    print(f"{(plus / len(arr)):0,.6f}")
    print(f"{(minus / len(arr)):0,.6f}")
    print(f"{((len(arr) - plus - minus) / len(arr)):0,.6f}")
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
