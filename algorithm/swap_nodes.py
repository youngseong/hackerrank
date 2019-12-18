#!/bin/python3

import os
import sys

#
# Complete the swapNodes function below.
#
def swapNodes(indexes, queries):
    def traverse(ind):
        lind, rind = indexes[ind-1]
        ltree = traverse(lind) if lind != -1 else []
        rtree = traverse(rind) if rind != -1 else []
        return ltree + [ind] + rtree
    
    def calc_depth():
        depths = [1] * (1 + len(indexes))
        depth2inds = {}

        q_ind = [1]
        while q_ind:
            ind = q_ind[0]
            q_ind.pop()
            depth = depths[ind]
            lind, rind = indexes[ind-1]

            if depth not in depth2inds:
                depth2inds[depth] = []
            depth2inds[depth].append(ind)

            if lind != -1:
                depths[lind] = depth + 1
                q_ind.append(lind)
            if rind != -1:
                depths[rind] = depth + 1
                q_ind.append(rind)
        return depths, depth2inds

    depths, depth2inds = calc_depth()
    d_max = max(depths)
    res = []
    return [[]]

    # switch children
    for k in queries:
        for nk in range(1, d_max, k):
            for ind in depth2inds[nk]:
                indexes[ind-1] = indexes[ind-1][::-1]
        res.append(traverse(1))
    
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()

