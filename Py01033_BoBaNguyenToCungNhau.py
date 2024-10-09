from math import *
l, r = map(int, input().split())
for i in range(l, r - 1):
    for j in range(i + 1, r):
        if gcd(i, j) == 1:
            for z in range(j + 1, r + 1):
                if gcd(i, z) == 1 and gcd(j, z) == 1:
                    print('(', end = "")
                    print(i, j, z, sep = ", ", end = "")
                    print(')')