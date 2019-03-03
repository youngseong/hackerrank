# https://www.hackerrank.com/challenges/magic-square-forming/problem

import math
import os
import random
import re
import sys

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    def dist(ans, s):
        d = 0
        for i in range(3):
            for j in range(3):
                d += abs(s[i][j] - ans[i][j])
        return d

    answers = [
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]]
        ]

    dists = []
    for ans in answers:
        for i in [-1, 1]:
            ans_ = ans[::i]
            dists.append(dist(ans_, s))
            for r in range(3):
                ans_[r] = ans_[r][::-1]
            dists.append(dist(ans_, s))

    return min(dists)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()

