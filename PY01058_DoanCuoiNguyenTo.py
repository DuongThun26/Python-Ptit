from math import sqrt
def nt(n):
    if n < 2: return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0: return False
    return True

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
        n = input()[-4:]
        m = 0
        for i in n:
            m = m * 10 + int(i)
        if nt(m): print('YES')
        else: print('NO')