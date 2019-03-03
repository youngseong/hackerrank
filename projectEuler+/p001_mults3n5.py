# #1: Multiples of 3 and 5

import sys

def nC2(n):
    return (n * (n+1)) // 2

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    n_3 = (n-1) // 3
    n_5 = (n-1) // 5
    n_3x5 = (n-1) // 15
    
    res= 3 * nC2(n_3) + 5 * nC2(n_5) - 15 * nC2(n_3x5)
    
    print(res)
