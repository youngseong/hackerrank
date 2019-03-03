# #3: Largest prime factor
# one case is failed by timeout

import sys
import math

def find_next_divisor(n, div):
    while div <= n:
        if n % div == 0:
            break
        div += 1
    return div

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())

    n_ = n
    
    max_div = 0
    div = 2
    while n_ > 1:
        div = find_next_divisor(n_, div)
        max_div = max(max_div, div)
        while n_ % div == 0:
            n_ /= div
    
    print(max_div)
