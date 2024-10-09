from math import *
def nt(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1
def tc(n):
    m = 0
    while n:
        m += n % 10
        n //= 10
    return m
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a, b = map(int, input().split())
        if nt(tc(gcd(a, b))): print('YES')
        else: print('NO')