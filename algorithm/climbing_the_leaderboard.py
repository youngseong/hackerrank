# https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    rank = 1
    j = -1
    N = len(alice)
    ranks = []
    prev_score = scores[0]

    for score in scores:
        if prev_score > score:
            rank += 1

        while j >= -N and alice[j] >= score:
            ranks.append(rank)
            j -= 1
        
        if j < -N:
            break

        prev_score = score

    rank += 1

    for _ in range(j, -len(alice)-1, -1):
        ranks.append(rank)

    return ranks[::-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

