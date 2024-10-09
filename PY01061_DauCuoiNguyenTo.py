from math import sqrt
def nt(n):
    if n < 2: return False
    for i in range (2, int(sqrt(n)) + 1):
        if n % i == 0: 
            return False
    return True

def check(n):
    dau = int(n[:3])
    cuoi = int(n[-3:])
    if nt(cuoi) and nt(dau):
        return True
    return False

if __name__ == "__main__":
    t = int(input())
    while t:
        t -= 1
        n = input()
        if check(n):
            print('YES')
        else:
            print('NO')