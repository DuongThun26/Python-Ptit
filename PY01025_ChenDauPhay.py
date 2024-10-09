n = list(input())
cnt = 1
for i in range(len(n) - 1, -1, -1):
    if cnt == 3:
        cnt = 1
        n.insert(i, ',')
    else:
        cnt += 1
if n[0] == ',': n.remove(',')
for i in n: print(i, sep = "", end = "")