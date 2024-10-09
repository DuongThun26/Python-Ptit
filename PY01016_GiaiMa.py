if __name__ == "__main__":
    t = int(input())
    while t:
        s = input()
        for i in range(0, len(s), 2):
            if s[i] >= 'A' and s[i] <= 'Z':
                for j in range(int(s[i + 1])):
                    print(s[i], end = "")
        print()
        t -= 1
