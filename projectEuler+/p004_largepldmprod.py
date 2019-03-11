# #4: Largest palindrom product
# need to look into failure cases

import math
import sys

def getLeft3Digits(n):
    abc = n // 1000
    a = abc // 100
    b = (abc % 100) // 10
    c = abc % 10
    
    return a, b, c

def isPldm(n):
    a, b, c = getLeft3Digits(n)
    cba = n % 1000
    cba_ = c * 100 + b * 10 + a
    
    return cba == cba_

def nextPldm(n):
    a, b, c = getLeft3Digits(n - 1000 if isPldm(n) else n - 1)
    abc = a * 100 + b * 10 + c
    cba = c * 100 + b * 10 + a
    
    return abc * 1000 + cba

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())

    finished = False
    n_ = n
    while n_ >= 1e5 and not finished:
        n_ = nextPldm(n_)
        
        for d in range(101, 1000):
            r = n_ // d
            if n_ % d == 0 and 100 <= r and r < 1000:
                finished = True
                break
    print(n_)

