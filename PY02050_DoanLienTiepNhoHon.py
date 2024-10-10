if __name__ == "__main__":
    t = int(input())
    while t:
        t -= 1
        n = int(input())
        a = list(map(int, input().split()))
        f = [1] * n
        stack = []
        for i in range(n):
            while stack and a[i] >= a[stack[-1]]:
                stack.pop()
            if stack:
                f[i] = i - stack[-1]
            else:
                f[i] = i + 1
            stack.append(i)
        for i in f:
            print(i, end = " ")
        print()