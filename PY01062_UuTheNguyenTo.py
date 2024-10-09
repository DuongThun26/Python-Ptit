from math import sqrt
a = ['2', '3', '5', '7']
def nt(n):
    if n < 2: return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0: return False
    return True
def check(n):
    if nt(len(n)) == False: return False
    demNt = 0
    demKNt = 0
    for i in range(len(n)):
        if n[i] in a: demNt += 1
        else: demKNt += 1
    return demKNt < demNt

if __name__ == "__main__":
    t = int(input())
    while t:
        t -= 1
        n = input()
        if check(n):
            print('YES')
        else: print('NO')