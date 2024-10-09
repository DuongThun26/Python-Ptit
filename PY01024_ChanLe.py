def check(n):
    s, r = n % 10, n % 10
    n //= 10
    while n:
        x = n % 10
        s += x
        if abs(x - r) != 2: return False
        n //= 10
        r = x
    if s % 10 != 0: return False
    return True

if __name__ == "__main__":
    t = int(input())
    while t:
        n = int(input())
        if check(n): print('YES')
        else: print('NO')
        t -= 1