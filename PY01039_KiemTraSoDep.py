def check(s):
    m = len(s)
    if m % 2 == 0:
        c = s[::-1]
        x = ord(s[m - 1]) + ord(c[m - 1])
        for i in range(m - 1):
            if ord(c[i]) + ord(s[i]) != x: return False
        return True
    else:
        c = s[::-1]
        return c == s    

if __name__ == "__main__":
    t = int(input())
    while t:
        t -= 1
        n = input()
        if check(n):
            print('YES')
        else: print('NO')