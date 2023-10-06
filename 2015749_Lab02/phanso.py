import math


class PhanSo:
    def __init__(self, tu: int, mau: int) -> None:
        if (mau == 0):
            raise Exception("Mẫu số phải khác 0")
        else:
            self.tu = tu
            self.mau = mau
            self.rut_gon()

    def gia_tri_ps(self) -> float:
        return self.tu / self.mau

    def rut_gon(self):
        uoc_chung = math.gcd(self.tu, self.mau)
        if uoc_chung != 1:
            self.tu = self.tu // uoc_chung
            self.mau = self.mau // uoc_chung

    def __add__(self, other):
        kq = PhanSo((self.tu * other.mau + other.tu *
                    self.mau), (self.mau * other.mau))
        kq.rut_gon()
        return kq

    def __sub__(self, other):
        kq = PhanSo((self.tu * other.mau - other.tu *
                    self.mau), (self.mau * other.mau))
        kq.rut_gon()
        return kq

    def __mul__(self, other):
        kq = PhanSo((self.tu * other.tu), (self.mau * other.mau))
        kq.rut_gon()
        return kq

    def __truediv__(self, other):
        kq = PhanSo((self.tu * other.mau), (self.mau * other.tu))
        kq.rut_gon()
        return kq

    def __str__(self):
        if self.mau == 1:
            return f"{self.tu}"
        return f"{self.tu}/{self.mau}"


# a = PhanSo(6, 1)
# # b = PhanSo(5, 6)
# a.rutGon()
# print(a)
# # print(f"{a} + {b} = {a+b}")
# # print(f"{a} - {b} = {a-b}")
# # print(f"{a} * {b} = {a*b}")
# # print(f"{a} / {b} = {a/b}")


class DanhSachPhanSo:
    def __init__(self) -> None:
        self.dsps = []

    def them_ps(self, *args: PhanSo):
        for ps in args:
            self.dsps.append(ps)

    def xuat_ps(self):
        for ps in self.dsps:
            print(ps, end="\n")

    def dem_ps_am(self):
        # count = 0
        # for i in self.dsps:
        #     if i.tu // i.mau < 0:
        #         count += 1
        # return count
        return sum(1 for ps in self.dsps if ps.gia_tri_ps() < 0)

    def tim_ps_duong_min(self):
        min = 999999999.0
        for ps in self.dsps:
            gtmin = ps.gia_tri_ps()
            if 0 < gtmin < min:
                min = gtmin
                result = ps
        return result

    def tim_vi_tri_ps_x(self, phan_so: PhanSo):
        result = []
        for i in range(len(self.dsps)):
            if self.dsps[i].gia_tri_ps() == phan_so.gia_tri_ps():
                result.append(i)
        return result

    def tong_ps_am(self):
        tong = PhanSo(0, 1)
        for ps in self.dsps:
            if ps.gia_tri_ps() < 0:
                tong += tong.__add__(ps)
        return tong

    def xoa_ps_x(self, phan_so: PhanSo):
        for ps in self.dsps:
            if ps.gia_tri_ps() == phan_so.gia_tri_ps():
                self.dsps.remove(ps)
                print(f"Xóa {ps} khỏi mảng")

    def xoa_ps_tu_x(self, tu: int):
        for ps in self.dsps:
            if ps.tu == tu:
                self.dsps.remove(ps)
                print(f"Xóa phân số có tử {tu}")

    def sap_xep_ps(self, daogt: bool = False):
        self.dsps.sort(key= lambda ps: ps.gia_tri_ps(), reverse=daogt)
    
    def sap_xep_ps_tu(self, daogt: bool = False):
        self.dsps.sort(key= lambda ps: ps.tu, reverse=daogt)
    
    def sap_xep_ps_mau(self, daogt: bool = False):
        self.dsps.sort(key= lambda ps: ps.mau, reverse=daogt)

ps1 = PhanSo(1, 3)
ps2 = PhanSo(5, 7)
ps3 = PhanSo(-5, 6)
ps4 = PhanSo(7, 1)
ps5 = PhanSo(-9, 3)
ps6 = PhanSo(1, 3)
ps7 = PhanSo(4, 3)
dsps = DanhSachPhanSo()
print("Danh sách phân số:")
dsps.them_ps(ps1, ps2, ps3, ps4, ps5, ps6, ps7)
dsps.xuat_ps()

print(f"Trong mảng có: {dsps.dem_ps_am()} phân số âm")

print(f"Phân số dương nhỏ nhất trong mảng: {dsps.tim_ps_duong_min()}")

phan_so_tim = PhanSo(1, 3)
print(f"Các vị trí của phân số {phan_so_tim} trong mảng:")
kq = dsps.tim_vi_tri_ps_x(phan_so_tim)
for i in kq:
    print(i)

print(f"Tổng các phân số âm trong mảng: {dsps.tong_ps_am()}")

phan_so_xoa = PhanSo(5, 7)
xoa = dsps.xoa_ps_x(phan_so_xoa)
print(f"Mảng sau khi xoá {phan_so_xoa}")
dsps.xuat_ps()

xoa_tu = 4
rmps = dsps.xoa_ps_tu_x(xoa_tu)
print(f"Mảng sau khi xoá phân số có tử {xoa_tu}")
dsps.xuat_ps()

print("Danh sách phân số sau khi được sắp xếp:")
print("Theo chiều tăng dần:")
dsps.sap_xep_ps()
dsps.xuat_ps()
print("Theo chiều giảm dần:")
dsps.sap_xep_ps(True)
dsps.xuat_ps()
print("Theo chiều tăng dần của tử:")
dsps.sap_xep_ps_tu()
dsps.xuat_ps()
print("Theo chiều giảm dần của tử:")
dsps.sap_xep_ps_tu(True)
dsps.xuat_ps()
print("Theo chiều tăng dần của mẫu:")
dsps.sap_xep_ps_mau()
dsps.xuat_ps()
print("Theo chiều giảm dần của mẫu::")
dsps.sap_xep_ps_mau(True)
dsps.xuat_ps()