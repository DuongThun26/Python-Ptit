from math import *
def check(n):
    if len(n) == 1: return False
    m = n[::-1]
    if m == n: return True
    return False
if __name__ == "__main__":
    t = int(input())
    while t:
        t -= 1
        n = input()
        s = 0
        for i in n:
            s += int(i)
        if check(str(s)) == True:
            print("YES")
        else:
            print("NO")
