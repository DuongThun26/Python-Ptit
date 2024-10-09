def lat(n):
    m = 0
    while n:
        m = m * 10 + n % 10
        n //= 10
    return m
def check(n, cnt):
    ans = n + lat(n)
    if cnt >= 1000: return -1
    if ans % 7 == 0: return ans
    else: return check(ans, cnt + 1)

if __name__ == "__main__":
    t = int(input())
    while t:
        t -= 1
        n = int(input())
        if n % 7 == 0: print(n)
        else: print(check(n, 0))