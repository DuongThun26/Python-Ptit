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
    def cong(self, p):
        bc = self.mauSo * p.mauSo // gcd(self.mauSo, p.mauSo)
        tu = self.tuSo * (bc // self.mauSo) + p.tuSo * (bc // p.mauSo)
        self.tuSo = tu
        self.mauSo = bc

if __name__ == "__main__":
    s = list(map(int, input().split()))
    p1 = PhanSo(s[0], s[1])
    p2 = PhanSo(s[2], s[3])
    p1.ToiGian()
    p2.ToiGian()
    p1.cong(p2)
    print(p1)