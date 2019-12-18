#!/bin/python3

import os
import sys

#
# Complete the swapNodes function below.
#
def swapNodes(indexes, queries):
    def traverse(ind, d, k):
        if d % k == 0:
            indexes[ind-1] = indexes[ind-1][::-1]

        lind, rind = indexes[ind-1]
        ltree = traverse(lind, d+1, k) if lind != -1 else []
        rtree = traverse(rind, d+1, k) if rind != -1 else []
        return ltree + [ind] + rtree
    
    res = []

    # switch children
    for k in queries:
        res.append(traverse(1, 1, k))
    
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

