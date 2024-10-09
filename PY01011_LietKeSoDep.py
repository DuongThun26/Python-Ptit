def check(n):
    if len(str(n)) % 2 == 1: return False
    tmp, m = n, 0
    while n:
        r = n % 10
        if r != 0 and r != 2 and r != 4 and r != 6 and r != 8: return False
        m = m * 10 + r
        n //= 10
    return m == tmp
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())
        for i in range(22, n):
            if check(i) == True:
                print(i, end = " ")
        print()