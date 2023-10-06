import datetime
from sinh_vien_chinh_quy import SinhVienChinhQuy
from sinh_vien_phi_chinh_quy import SinhVienPhiChinhQuy
from sinhvien import SinhVien

class DanhSachSV:
    def __init__(self):
        self.dssv = []

    def them_sv(self, sv: SinhVien):
        self.dssv.append(sv)

    def xuat_sv(self):
        for sv in self.dssv:
            print(sv)

    def tim_sv_theo_ms(self, mssv: int):
        for i in range(len(self.dssv)):
            if self.dssv[i].mssv == mssv:
                return i
        else:
            return -1
    
    def tim_sv_theo_loai(self, loai: str):
        if loai == "chinhquy":
            return [sv for sv in self.dssv if isinstance(sv, SinhVienChinhQuy)]
        return [sv for sv in self.dssv if isinstance(sv, SinhVienPhiChinhQuy)]
    
    def tim_diemRL_sv_tren(self, diem_rl: int):
        return [sv for sv in self.dssv if isinstance(sv, SinhVienChinhQuy) and sv.diemRL > diem_rl]

    def tim_sv_theo_trinh_do_va_truoc_ngay(self, trinh_do: str, ngay_tk: datetime):
        return [sv for sv in self.dssv if isinstance(sv, SinhVienPhiChinhQuy)
                and sv.trinhDo == trinh_do
                and sv.ngaySinh < ngay_tk
                ]
