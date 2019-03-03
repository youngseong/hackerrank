# https://www.hackerrank.com/challenges/non-divisible-subset/problem

import math
import os
import random
import re
import sys

# Complete the nonDivisibleSubset function below.
def nonDivisibleSubset(k, S):
    modcnts = [0] * k

    for s in S:
        modcnts[s % k] += 1
    
    maxsz = 0

    def elementCount(i):
        return modcnts[i] if 2*i % k != 0 else 1

    print(modcnts)

    if modcnts[0]:
        maxsz += 1

    mid = k // 2
    print(mid)
    for i in range(1, mid+1):
        n0 = i
        n1 = (k-i) % k

        print(n0, modcnts[n0])
        print(n1, modcnts[n1])

        if n0 == n1:
            maxsz += 1
        else:
            maxsz += max(modcnts[n0], modcnts[n1])
    
    return maxsz


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    S = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, S)

    fptr.write(str(result) + '\n')

    fptr.close()

