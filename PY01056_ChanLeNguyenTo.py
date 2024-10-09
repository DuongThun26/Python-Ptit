from math import *
def check(n):
    if n < 2: return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0: return False
    return True
def kt(n):
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])
        if i % 2 == 0:
            if int(n[i]) % 2 == 0:
                continue
            else:
                return False
        else:
            if int(n[i]) % 2 == 1:
                continue
            else:
                return False
    if check(sum):
        return True
    else:
        return False
if __name__ == "__main__":
    t = int(input())
    while t:
        t-= 1
        n = input()
        if kt(n):
            print('YES')
        else:
            print('NO')