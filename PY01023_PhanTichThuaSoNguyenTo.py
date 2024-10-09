from math import *
t = int(input())
while t:
    n = int(input())
    print('1 ', sep = "", end = "")
    for i in range(2, isqrt(n) + 1):
        if n %  i == 0:
            cnt = 0
            while n %  i == 0:
                cnt += 1
                n //= i
            print(" * ", i, '^', cnt, sep = "", end = "")
    if n > 1: print(" * ", n, "^1", sep = "", end = "")
    print()
    t -= 1