
if __name__ == "__main__":
    t = int(input())
    while t:
        t -= 1
        s = input()
        n = input()
        cnt = 0
        i = 0
        while i <= len(s) - len(n):
            if s[i:i + len(n)] == n:
                cnt += 1
                i += len(n)
            else: i += 1
        print(cnt)
