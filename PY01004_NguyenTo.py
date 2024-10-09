from math import *
def cnt(n):
    dem = 0
    for i in range(1, n):
        if gcd(n, i) == 1: dem += 1
    return dem
def nt(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        if nt(cnt(n)): print('YES')
        else: print('NO')