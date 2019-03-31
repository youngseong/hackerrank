# https://www.hackerrank.com/challenges/coin-change/problem

import math
import os
import random
import re
import sys

# Complete the getWays function below.
def getWays(n, c):
    sumcounts = [0] * (n+1)

    for penny in c:
        if penny > n:
            continue
            
        cost = penny
        sumcounts[cost] += 1

        for i in range(n-cost+1):
            cost = i + penny
            if sumcounts[i] > 0:
                sumcounts[cost] += sumcounts[i]
        
        # print(sumcounts)
    return sumcounts[n]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(n, c)
    fptr.write(str(ways))

    fptr.close()

