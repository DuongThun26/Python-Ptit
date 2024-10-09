def tc(n, x, m):
    cnt = 0
    for i in range(int((m - n) / x)):
        ans = n + n * x / 100
        if n >= m: return cnt
        cnt += 1
        n = ans
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, x, m = map(float, input().split())
        print(tc(n, x, m))
