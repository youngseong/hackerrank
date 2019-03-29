# https://www.hackerrank.com/challenges/find-the-running-median/problem

import os
import sys

def runningMedian(a):
    lower = [] # max heap
    upper = [] # min heap

    def insert_(heap, val):
        heap.append(val)

        # sift_up
        ind = len(heap)-1
        while ind > 0:
            parent = (ind-1) // 2
            if heap[parent] < heap[ind]:
                heap[parent], heap[ind] = heap[ind], heap[parent]
                ind = parent
            else:
                break
    
    def sift_down(heap, start):
        root = start
        N = len(heap)
        while 2 * root + 1 < N:
            left = 2 * root + 1
            right = left + 1

            ind = root
            if heap[root] < heap[left]:
                ind = left
            if right < N and heap[ind] < heap[right]:
                ind = right
            if ind == root:
                return

            heap[root], heap[ind] = heap[ind], heap[root]
            root = ind

    def insert(val):
        if len(lower) == 0:
            lower.append(val)
            return
        
        if val >= lower[0]:
            insert_(upper, -val)
        else:
            insert_(lower, val)
    
    def equalize():
        n_lower, n_upper = len(lower), len(upper)

        if n_lower - n_upper > 1:
            lower[0], lower[-1] = lower[-1], lower[0]
            val = lower.pop()
            sift_down(lower, 0)
            insert_(upper, -val)
        elif n_upper - n_lower > 1:
            upper[0], upper[-1] = upper[-1], upper[0]
            val = upper.pop()
            sift_down(upper, 0)
            insert_(lower, -val)

    medians = []

    for elem in a:
        insert(elem)
        # print('before balancing')
        # print(lower, upper)

        equalize()
        # print('after balancing')
        # print(lower, upper)

        n_lower, n_upper = len(lower), len(upper)

        median = 0.0
        if n_lower > n_upper:
            median += lower[0]
        elif n_lower < n_upper:
            median -= upper[0]
        else:
            median = (lower[0] - upper[0]) / 2

        medians.append(median)

    return medians


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input())

    a = []

    for _ in range(a_count):
        a_item = int(input())
        a.append(a_item)

    result = runningMedian(a)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

