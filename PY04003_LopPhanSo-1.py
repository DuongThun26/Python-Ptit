from math import *
class PhanSo:
    def __init__(self, tu, mau):
        self.tuSo = tu
        self.mauSo = mau
    def ToiGian(self):
        ucln = gcd(self.tuSo, self.mauSo)
        self.tuSo //= ucln
        self.mauSo //= ucln
    def __str__(self):
        return f'{self.tuSo}{"/"}{self.mauSo}'
if __name__ == "__main__":
    s = list(map(int, input().split()))
    p = PhanSo(s[0], s[1])
    p.ToiGian()
    print(p)