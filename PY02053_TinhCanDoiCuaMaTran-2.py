if __name__ == "__main__":
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    k = int(input())
    tongTren, tongDuoi = 0, 0
    for i in range(n):
        for j in range(n):
            if j < n - 1 - i:
                tongTren += a[i][j]
            elif j > n - 1 - i:
                tongDuoi += a[i][j]
    if abs(tongTren - tongDuoi) <= k:
        print('YES')
    else:
        print('NO')
    print(abs(tongTren - tongDuoi))