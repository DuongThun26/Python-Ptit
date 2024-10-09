n = input()
cnt = 0
for i in n:
    if i == '4' or i == '7': cnt+= 1
if cnt == 7 or cnt == 4: print('YES')
else: print('NO')