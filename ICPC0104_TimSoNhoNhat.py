def search(s):
    minn = 10000000
    tmp = 0
    for i in range(len(s)):
        if s[i] >= '0' and s[i] <= '9':
            tmp = tmp * 10 + (ord(s[i]) - ord('0'))
        else:
            if tmp != 0:
                minn = min(minn, tmp)
            tmp = 0
    return minn
if __name__ == "__main__":
    t = int(input())
    while t:
        t -= 1
        s = input()
        s += "#"
        ans = search(s)
        print(ans)