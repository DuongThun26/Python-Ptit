t = int(input())
while t:
    n = input()
    x = n[len(n) - 2] + n[len(n) - 1]
    if x == '86': print('YES')
    else: print('NO')
    t -= 1