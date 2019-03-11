# #7: 10001st prime

import sys

primes = [2,3,5,7,11,13,17,19,23,29]

i = primes[-1]
while len(primes) < 10000:
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

    print(primes[n-1])

