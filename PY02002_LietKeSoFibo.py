t = int(input())
f = [0] * 94
f[1] = 1
f[2] = 1
for i in range(3, 94):
    f[i] = f[i - 2] + f[i - 1]
while t:
    t -= 1
    a, b = map(int, input().split())
    for i in range(a, b + 1):
        print(f[i], end = " ")
    print()