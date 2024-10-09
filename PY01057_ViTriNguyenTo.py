from math import sqrt
def nt(n):
    if n < 2: return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0: return False
    return True

a = ['2', '3', '5', '7']
def check(n):
    for i in range(len(n)):
        if nt(i) == False and n[i] in a:
            return False
        elif nt(i) == True and n[i] not in a:
            return False
    return True

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
        n = input()
        if check(n):
            print('YES')
        else:
            print('NO')