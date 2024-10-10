if __name__ == "__main__":
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]   
    k = int(input())
    tongTren = 0
    tongDuoi = 0
    for i in range(n):
        for j in range(n):
            if j > i:
                tongTren += a[i][j]
    for i in range(n):
        for j in range(n):
            if j < i:
                tongDuoi += a[i][j]
    if abs(tongTren - tongDuoi) <= k:
        print('YES')
    else:
        print('NO')
    print(abs(tongTren - tongDuoi))