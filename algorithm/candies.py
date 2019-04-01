# https://www.hackerrank.com/challenges/candies/problem

import math
import os
import random
import re
import sys

# Complete the candies function below.
def candies(n, arr):
    cs = [0] * n

		# set 1 for each local minima
    for i in range(n):
        if (i == 0 or arr[i] <= arr[i-1]) and (i+1 == n or arr[i] <= arr[i+1]):
            cs[i] = 1
    
		# forward sweep
    for i in range(1, n):
        if cs[i-1] != 0 and arr[i] > arr[i-1]:
            cs[i] = max(cs[i], cs[i-1] + 1)

    # backward sweep
    for i in range(n-2, -1, -1):
        if cs[i+1] != 0 and arr[i] > arr[i+1]:
            cs[i] = max(cs[i], cs[i+1] + 1)

    # print(cs)
    
    return sum(cs)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

