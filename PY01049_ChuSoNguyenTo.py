from math import *
def nt(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True
def check(n):
    if nt(len(n)) == False:
        return False
    cnt = 0
    for i in n:
        if i == '2' or i == '3' or i == '5' or i == '7':
            cnt += 1
    return cnt > (len(n) - cnt)
if __name__ == "__main__":
    t = int(input())
    while t:
        t -= 1
        n = input()
        if check(n):
            print('YES')
        else:
            print('NO')
