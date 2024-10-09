from math import *
t = int(input())
for i in range(t):
    n = input()
    m = int(n)
    if m > 10:
        cnt = 0
        while m >= 10:
            cnt += 1
            if m % 10 >= 5:
                m = ceil(m / 10)
            else:
                m = round(m / 10)
        print(m * (10 ** cnt))
    else: print(m)