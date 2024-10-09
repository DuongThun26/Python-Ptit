from math import *
def nt(n):
    if n < 2: return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True
if __name__ == "__main__":
    t = int(input())
    while t:
        t -= 1
        s = input()
        a = int(s[-4:])
        if nt(a):
            print('YES')
        else:
            print('NO')