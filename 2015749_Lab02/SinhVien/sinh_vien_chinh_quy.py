from sinhvien import SinhVien
import datetime

class SinhVienChinhQuy(SinhVien):
    def __init__(self, ma_so: int, ho_ten: str, ngay_sinh: datetime, diem_RL: int):
        super().__init__(ma_so, ho_ten, ngay_sinh)
        self.__diemRL = diem_RL

    def __str__(self):
        return super().__str__() + f"\t{self.__diemRL}"