def check(s):
    for i in range(len(s) - 1):
        if int(s[i]) >= int(s[i + 1]):
            return False
    return True
if __name__ == "__main__":
    t = int(input())
    while(t > 0):
        t -= 1
        s = input()
        if len(s) < 3:
            print('NO')
        else:
            index = 0
            for i in range(len(s) - 1):
                if int(s[i + 1]) > int(s[i]):
                    continue
                else:
                    index = i + 1
                    break
            x = s[index:]
            x = x[::-1]
            if check(x):
                print('YES')
            else:
                print('NO')
