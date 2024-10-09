if __name__ == "__main__":
    t = int(input())
    while t:
        s = input()
        a, b = s[0] + s[1], s[len(s) - 2] + s[len(s) - 1]
        if a == b: print('YES')
        else:
            print('NO')
        t -= 1