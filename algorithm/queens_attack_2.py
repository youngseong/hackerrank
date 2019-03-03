# https://www.hackerrank.com/challenges/queens-attack-2/problem

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    # vec_r = i // 3 - 1
    # vec_c = i % 3 - 1

    dirs = [[-1,-1], [-1,0], [-1,1],
            [0,-1], [0,0], [0,1],
            [1,-1], [1,0], [1,1]]
    bnds = [[0,0]] * len(dirs)

    for i in range(len(dirs)):
        d = dirs[i]

        dr = (n+1 - r_q) if d[0] > 0 else r_q
        dc = (n+1 - c_q) if d[1] > 0 else c_q
        if d[0] * d[1] != 0:
            dr = dc = min(dr, dc)
        bnds[i] = [r_q + d[0] * dr, c_q + d[1] * dc]

    for obs in obstacles:
        dr = obs[0] - r_q
        dc = obs[1] - c_q

        if dr * dc != 0 and abs(dr / dc) != 1:
            continue

        # get i
        nr = 0 if dr == 0 else dr/abs(dr)
        nc = 0 if dc == 0 else dc/abs(dc)

        i = int(nr+1) * 3 + int(nc+1)

        bnd = bnds[i]

        # update bnd
        if dr:
            bnd[0] = obs[0] if (bnd[0] - r_q) / dr > 1 else bnd[0]
        if dc:
            bnd[1] = obs[1] if (bnd[1] - c_q) / dc > 1 else bnd[1]

    n = 0
    for bnd in bnds:
        dr = abs(bnd[0] - r_q)
        dc = abs(bnd[1] - c_q)
        d = 0
        if dr:
            d = dr - 1
        elif dc:
            d = dc - 1
        n += d
    return n

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ob = input().split()

    r_q = int(ob[0])

    c_q = int(ob[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()

