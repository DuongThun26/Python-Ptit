def check(n):
    if len(n) % 2 == 1 or n != n[::-1]: return False
    for i in range(len(n)):
        if int(n[i]) % 2 == 1:
            return False
    return True

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())
        for i in range(22, n, +2):
            if check(str(i)):
                print(i, end = " ")
        print()