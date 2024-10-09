if __name__ == "__main__":
    t = int(input())
    while t:
        s = input()
        cnt = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                cnt += 1
            else:
                print(cnt, s[i - 1], sep = "", end = "")
                cnt = 1
        if cnt >= 1: print(cnt, s[len(s) - 1], sep = "", end = "")
        t -= 1
        print()
