from math import *
t = int(input())
while t:
    n = int(input())
    tmp = n
    m = 0
    while tmp:
        m = m * 10 + tmp % 10
        tmp //= 10
    if gcd(m, n) == 1: print('YES')
    else: print('NO')
    t -= 1