def Try(b, i, used, a, n):
    for j in range(n):
        if used[j] == 0:
            a[i] = j
            used[j] = 1
            if i == n - 1:
                for x in range(n):
                    print(b[a[x]], end = "")
                print()
            else:
                Try(b, i + 1, used, a, n)
            used[j] = 0

if __name__ == "__main__":
    b = list(input())
    n = len(b)
    used = [0] * (n + 1)
    a = [''] * (n + 1)
    Try(b, 0, used, a, n)