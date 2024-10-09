t = int(input())
for i in range(t):
    n = input()
    ok = False
    for i in n:
        if i != '4' and i != '7': 
            print('NO')
            ok = True
            break
    if ok == False: print('YES') 
