def Tower(n, A, B, C):
    if n == 1:
        print(A, '->', C)
    else:
        Tower(n - 1, A, C, B)
        Tower(1, A, B, C)
        Tower(n - 1, B, A, C)
if __name__ == "__main__":
    n = int(input())
    Tower(n, 'A', 'B', 'C')