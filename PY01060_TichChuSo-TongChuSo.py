t = int(input())
while t > 0:
    t -= 1
    n = input()
    tichChan = 1
    tongLe = 0
    for i in range(len(n)):
        if i % 2 == 0:
            if int(n[i]) != 0:
                tichChan *= int(n[i])
        else:
            tongLe += int(n[i])
    print(tichChan, tongLe)