from math import *
def nt(n):
    if n < 2: return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
if __name__ == "__main__":
    n = int(input())
    s = 0
    while n:
        n -= 1
        x = int(input())
        if nt(x): s += x
        else:
            for i in range(2, int(sqrt(x)) + 1):
                while x % i == 0:
                    s += i
                    x //= i
            if x != 1:
                s += x
    print(s)