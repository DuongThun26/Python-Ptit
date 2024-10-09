def check(s):
    s = list(s)
    x = s[::-1]
    for i in range(1, len(s)):
        if int(abs(ord(s[i]) - ord(s[i - 1]))) != int(abs(ord(x[i]) - ord(x[i - 1]))):
            return False
    return True
if __name__ == "__main__":
    t = int(input())
    while t:
        s = input()
        if check(s): print('YES')
        else: print('NO')
        t -= 1