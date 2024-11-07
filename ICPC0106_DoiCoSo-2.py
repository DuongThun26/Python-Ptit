from math import *

def heSo4(x):
    st = []
    cnt = 0
    res = 0
    for i in range(len(x) - 1, -1, -1):
        cnt += 1
        if(x[i] == '1'):
            res += 2 ** (cnt - 1)
        if cnt == 2:
            st.append(res)
            cnt = 0
            res = 0
        if i == 0 and res > 0:
            st.append(res)
    re = ""
    st = st[::-1]
    for i in range(len(st)):
        re += str(st[i])
    return re

def heSo8(x):
    st = []
    cnt = 0
    res = 0
    for i in range(len(x) - 1, -1, -1):
        cnt += 1
        if(x[i] == '1'):
            res += 2 ** (cnt - 1)
        if cnt == 3:
            st.append(res)
            cnt = 0
            res = 0
        if i == 0 and res > 0:
            st.append(res)
    re = ""
    st = st[::-1]
    for i in range(len(st)):
        re += str(st[i])
    return re

def heSo16(x):
    st = []
    cnt = 0
    res = 0
    for i in range(len(x) - 1, -1, -1):
        cnt += 1
        if(x[i] == '1'):
            res += 2 ** (cnt - 1)
        if cnt == 4:
            st.append(res)
            cnt = 0
            res = 0
        if i == 0 and res > 0:
            st.append(res)
    re = ""
    st = st[::-1]
    for i in range(len(st)):
        if st[i] >= 0 and st[i] <= 9: 
            re += str(st[i])
        else:
            re += chr(ord('A') + (st[i] - 10))
    return re

if __name__ == "__main__":
    t = int(input())
    while t:
        t -= 1
        coSo = int(input())
        x = input()
        if coSo == 2: print(x)
        elif coSo == 4: print(heSo4(x))
        elif coSo == 8: print(heSo8(x))
        else: print(heSo16(x))
        print()
# 2
# 8
# 10010100010010101
# 2
# 10010100010010101