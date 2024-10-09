if __name__ == "__main__":
    t = int(input())
    while t:
        t-= 1
        s = input()
        sum = 1
        for i in s:
            if i != '0':
                sum *= int(i)
        print(sum)