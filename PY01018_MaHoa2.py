P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
def tk(s):
    for i in range(len(P)):
        if s == P[i]:
            return i
    
if __name__ == "__main__":
    while True:
        s = input().split()
        k = int(s[0])
        if k == 0: break
        x = []
        for i in range(0, len(s[1])):
            c = tk(s[1][i])
            r = P[(c + k) % 28]
            x.append(r)
        for i in range(len(x) - 1, -1, -1):
            print(x[i], sep = "", end = "")
        print()