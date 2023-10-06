from sinhvien import SinhVien
import datetime

class SinhVienPhiChinhQuy(SinhVien):
    def __init__(self, ma_so: int, ho_ten: str, ngay_sinh: datetime, trinh_do: str, tgdt: str):
        super().__init__(ma_so, ho_ten, ngay_sinh)
        self.__thoiGianDaoTao = tgdt
        self.__trinhDo = trinh_do
    
    def __str__(self):
        return super().__str__() + f"\t{self.__trinhDo}\t{self.__thoiGianDaoTao}"