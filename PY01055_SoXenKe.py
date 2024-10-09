def check(s):
    if len(s) % 2 == 0:
        return False
    if s[0] == s[1]: return False
    for i in range(0, len(s) - 2, 2):
        if s[i] != s[i + 2]:
            return False
    return True
if __name__ == "__main__":
    t = int(input())
    while t:
        t -= 1
        s = input()
        if check(s):
            print('YES')
        else:
            print('NO')