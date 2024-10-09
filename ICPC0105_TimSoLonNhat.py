def search(s):
    ans = 0
    tmp = 0
    for i in range(len(s)):
        if s[i] >= '0' and s[i] <= '9':
            tmp = tmp * 10 + (ord(s[i]) - ord('0'))
        else:
            ans = max(ans, tmp)
            tmp = 0
    return ans
if __name__ == "__main__":
    t = int(input())
    while t:
        t -= 1
        s = input()
        s += "#"
        ans = search(s)
        print(ans)