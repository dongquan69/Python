from datetime import datetime
class SinhVien:
    truong = "Trường Đại học Đà Lạt"
    def __init__(self, *args) -> None:
        if len(args) == 3:
            self.__maSo: int = args[0]
            self.__hoTen: str = args[1]
            self.__ngaySinh: datetime = self.dateParse(args[2])
        elif len(args) == 1:
            dong = args[0].strip().split(',')
            self.__maSo: int = dong[0]
            self.__hoTen: str = dong[1]
            self.__ngaySinh: datetime = self.dateParse(dong[2])

    @property
    def maSo(self):
        return self.__maSo
    
    @property
    def hoTen(self):
        return self.__hoTen
    
    @property
    def ngaySinh(self):
        return self.__ngaySinh

    @maSo.setter
    def maSo(self, maSo):
        if self.ktMaSo(maSo):
            self.__maSo = maSo

    @staticmethod
    def ktMaSo(maSo: int):
        return len(str(maSo)) == 7

    @staticmethod
    def dateParse(date: str):
        return datetime.strptime(date, '%d/%m/%Y')

    @classmethod
    def doiTenTruong(self, tenMoi):
        self.truong = tenMoi


    def __str__(self) -> str:
        return f"{self.__maSo}\t{self.__hoTen}\t{self.__ngaySinh}"
    
    def xuat(self):
        print(f"{self.__maSo}\t{self.__hoTen}\t{self.__ngaySinh}")

# sv = SinhVien(2000000, "Nguyễn Văn ABC", "11/7/2002")
# sv.maSo = 3014789
# sv.xuat()   

class DanhSachSV:
    def __init__(self) -> None:
        self.dssv = []
    
    def themSV(self, sv: SinhVien):
        self.dssv.append(sv)
    
    def DocFile(self, tenfile):
        f = open(tenfile, "r", encoding='UTF-8')
        ls = f.readlines()
        for i in ls:
            self.dssv.append(SinhVien(i))

    def xuat(self):
        for sv in self.dssv:
            print(sv)

    def timSVTheoMSSV(self, mssv: int):
        return [sv for sv in self.dssv if sv.maSo == mssv]

    def timVTSVTheoMSSV(self, mssv: int):
        for i in range(len(self.dssv)):
            if self.dssv[i].maSo == mssv:
                return i
        return -1
    
    def xoaSVTheoMSSV(self, maSo: int) -> bool:
        vt = self.timVTSVTheoMSSV(maSo)
        if vt != -1:
            del self.dssv[vt]
            return True
        else:
            return False
    
    def timSVTheoTen(self, ten: str):
        return [sv for sv in self.dssv if sv.hoTen.split(' ')[-1].lower() == ten.lower()]

    def timSVSinhTruocNgay(self, ngay: str):
        return [sv for sv in self.dssv if sv.ngaySinh <= sv.dateParse(ngay)]
 
# sv1 = SinhVien(2033333, "Nguyễn Văn A", "12/8/2002")
# sv2 = SinhVien(2044444, "Nguyễn Văn B", "13/9/2002")
# sv3 = SinhVien(2055555, "Nguyễn Văn C", "14/10/2002")
# sv4 = SinhVien(2066666, "Nguyễn Văn D", "15/11/2002")
# sv5 = SinhVien(2077777, "Nguyễn Văn E","16/12/2002")
dssv = DanhSachSV()
# dssv.themSV(sv1)
# dssv.themSV(sv2)
# dssv.themSV(sv3)
# dssv.themSV(sv4)
# dssv.themSV(sv5)
# dssv.xuat()

# mssv=2033333
# kq = dssv.timSVTheoMSSV(mssv)
# print(f"\nSinh vien co ma so {mssv}")
# for kqsv in kq:
#     print(kqsv)

# mssv = 2055555
# vt = dssv.timVTSVTheoMSSV(mssv)
# print(f"\nSinh vien co ma so {mssv} o vi tri: {vt}")

print("Danh sách sinh viên:")
dssv.DocFile("data.txt")
dssv.xuat()

ten = "Hiếu"
kq = dssv.timSVTheoTen(ten)
print(f"\nSinh viên có tên {ten}:")
for sv in kq:
    print(sv)

ngayTK = "5/11/2002"
kq = dssv.timSVSinhTruocNgay(ngayTK)
print(f"\nSinh viên sinh trước ngày {ngayTK} ")
for sv in kq:
    print(sv)





            



        
    