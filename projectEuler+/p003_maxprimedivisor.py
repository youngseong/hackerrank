# #3: Largest prime factor

import sys
import math

def find_next_divisor(n, div):
    while div * div <= n:
        if n % div == 0:
            break
        div += 2
    return div

def div_iter(n, div):
    while n % div == 0:
        n = n // div
    # print(div, n)
    return n

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())

    n_ = n

    max_div = div = 2
    if n_ % 2 == 0:
        n_ = div_iter(n_, div)

    div = 3
    while n_ > 1 and div * div <= n_:
        div = find_next_divisor(n_, div)
        max_div = max(max_div, div)
        n_ = div_iter(n_, div)

    max_div = max(max_div, n_)

    print(max_div)
