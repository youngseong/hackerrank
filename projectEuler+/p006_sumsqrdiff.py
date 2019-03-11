# #6: Sum square difference

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    sum_sqr = (n * (n+1) // 2) ** 2
    sqr_sum = n * (n+1) * (2*n+1) // 6
    
    print(sum_sqr - sqr_sum)
