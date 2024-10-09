class Rectangle:
    def __init__(self, chieuDai, chieuRong, mau):
        self.chieuDai = chieuDai
        self.chieuRong = chieuRong
        self.mau = mau
    def perimeter(self):
        chuVi = (self.chieuDai + self.chieuRong) * 2
        return chuVi
    def area(self):
        return self.chieuDai * self.chieuRong
    def color(self):
        return str(self.mau).title()

arr = input().split()
if int(arr[0]) > 0 and int(arr[1]) > 0:
    r = Rectangle(int(arr[0]), int(arr[1]), str(arr[2]))
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
else:
    print("INVALID")