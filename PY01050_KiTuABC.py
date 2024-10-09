def Try(a, b, i, n, d1, d2, d3):
    for j in range(1, 4):
        a[i] = j
        if j == 1: d1 += 1
        elif j == 2: d2 += 1
        else: d3 += 1
        if i == n and d1 <= d2 and d2 <= d3 and d1 >= 1:
            for x in range(1, n + 1):
                print(b[a[x] - 1], end = "")
            print()
        elif i > n: return
        else:
            Try(a, b, i + 1, n, d1, d2, d3)
        if j == 1: d1 -= 1
        elif j == 2: d2 -= 1
        else: d3 -= 1

if __name__ == "__main__":
    n = int(input())
    a = [0] * (n + 3)
    b = ['A', 'B', 'C']
    for i in range(3, n + 1):
        Try(a, b, 1, i, 0, 0, 0)