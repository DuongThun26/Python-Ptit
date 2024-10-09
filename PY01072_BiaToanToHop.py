ok = True
def init(b, n, k):
    for i in range(k):
        b.append(i + 1)
def Next(b, n, k):
    global ok 
    i = k - 1
    while i >= 0 and b[i] == n - k + i + 1:
        i -= 1
    if i >= 0:
        b[i] = b[i] + 1
        for j in range(i + 1, k):
            b[j] = b[i] + j - i
    else:
        ok = False
def results(s, b, k):
    for i in range(k):
        print(s[b[i] - 1], end = " ")
    print()
    
 
if __name__ == "__main__":
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    s = set(a)
    a = list(s)
    a.sort()
    b = []
    init(b, n, k)
    while ok == True:
        results(a, b, k)
        Next(b, len(s), k)


