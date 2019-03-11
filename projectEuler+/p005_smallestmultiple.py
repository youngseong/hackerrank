# #5: Smallest multiple

import sys

def findDivisor(n, div):
    while n != 1 and n % div != 0:
        div += 1
    return div

def getExp(n, div):
    cnt = 0
    while n % div == 0:
        n //= div
        cnt += 1
    return cnt

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    n_ = n
    exps = [0] * (n-1)
    for i in range(2, n+1):
        i_ = i
        div = 2
        while i_ > 1:
            cnt = getExp(i_, div)
            exps[div-2] = max(exps[div-2], cnt)
            i_ = i_ // (div ** cnt)
            div = findDivisor(i_, div)
    
    ret = 1
    for i in range(2, n+1):
        ret *= i ** exps[i-2]
    print(ret)

