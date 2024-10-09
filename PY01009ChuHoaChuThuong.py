if __name__ == "__main__":
    s = input()
    c, l = 0, 0
    for i in range(len(s)):
        if s[i] >= 'a' and s[i] <= 'z':
            c += 1
        elif s[i] >= 'A' and s[i] <= 'Z':
            l += 1
    if c >= l: print(s.lower())
    else: print(s.upper())