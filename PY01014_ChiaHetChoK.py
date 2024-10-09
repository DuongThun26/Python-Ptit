from math import *
if __name__ == '__main__':
    a, k, n = map(int, input().split())
    x = (a + k - 1) // k
    ok = True
    if a < n and x * k != a: 
        for i in range(x, n // k + 1):
            print(i * k - a, end = " ")
            ok = False
    if ok: print(-1)