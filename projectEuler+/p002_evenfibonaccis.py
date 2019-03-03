# #2: Even Fibonacci numbers

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    s = 0
    a = 1
    b = 2
    while b <= n:
        if b % 2 == 0:
            s += b
        c = a + b
        a = b
        b = c
    print(s)
