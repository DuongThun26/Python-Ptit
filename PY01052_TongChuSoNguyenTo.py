from math import *
def check(n):
    if n < 2: return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0: return False
    return True
if __name__ == "__main__":
    t = int(input())
    while t:
        t -= 1
        n = input()
        s = 0
        for i in n:
            s += int(i)
        if check(s) == True:
            print("YES")
        else:
            print("NO")
