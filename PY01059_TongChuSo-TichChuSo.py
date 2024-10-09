t = int(input())
while t > 0:
    t -= 1
    n = input()
    tongChan = 0
    tichLe = 1
    check = False
    for i in range(len(n)):
        if i % 2 == 0:
            tongChan += int(n[i])
        else:
            if int(n[i]) != 0:
                tichLe *= int(n[i])
                check = True
    print(tongChan, end = " ")
    if check: print(tichLe)
    else: print(0)