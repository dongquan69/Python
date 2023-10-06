import datetime

class SinhVien:
    truong = "Đại học Đà Lạt"
    def __init__(self, ma_so: int, ho_ten: str, ngay_sinh: datetime):
        self.__maSo = ma_so
        self.__hoTen = ho_ten
        self.__ngaySinh = ngay_sinh
    
    @property
    def hoTen(self):
        return self.__hoTen

    @hoTen.setter
    def hoTen(self, ho_ten: str):
        self.__hoTen = ho_ten

    @property
    def mssv(self):
        return self.__maSo

    @mssv.setter
    def mssv(self, ma_so: int):
        if self.kt_mssv(ma_so):
            self.__maSo = ma_so

    @staticmethod
    def kt_mssv(mssv: int):
        return len(str(mssv)) == 7

    def __str__(self):
        return f"{self.__maSo}\t{self.__hoTen}\t{self.__ngaySinh}"
    
    # def xuat(self):
    #     print(f"{self.__maSo}\t{self.__hoTen}\t{self.__ngaySinh}")
        
