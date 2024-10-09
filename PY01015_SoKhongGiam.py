if __name__ == "__main__":
    t = int(input())
    while t:
        n = input()
        ok = True
        for i in range(len(n) - 1):
            if int(n[i]) > int(n[i + 1]):
                ok =  False
                print('NO')
                break
        if ok: print('YES')
        t -= 1