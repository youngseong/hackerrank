# https://www.hackerrank.com/challenges/flipping-the-matrix/problem

import math
import os
import random
import re
import sys

# Complete the flippingMatrix function below.
def flippingMatrix(matrix):
    N = len(matrix)
    n = N // 2
    s = 0
    for r in range(n):
        for c in range(n):
            r_opp = N-1-r
            c_opp = N-1-c
            s += max(matrix[r][c],
                     matrix[r][c_opp],
                     matrix[r_opp][c],
                     matrix[r_opp][c_opp])
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        matrix = []

        for _ in range(2*n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()

