# #10: Summation of primes

import sys
from bisect import bisect_left

primes = [2, 3]
N = 10**6

i = primes[-1]
while i <= N:
    i += 2
    is_prime = True
    for p in primes:
        if i % p == 0:
            is_prime = False
            break
        if p * p > i:
            break
    if is_prime:
        primes.append(i)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    ind = bisect_left(primes, n)
    s = sum(primes[:ind]) + (n if primes[ind] == n else 0)
    print(s)
