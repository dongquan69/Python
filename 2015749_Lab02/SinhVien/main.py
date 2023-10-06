from datetime import datetime

from sinhvien import SinhVien
from sinh_vien_chinh_quy import SinhVienChinhQuy
from sinh_vien_phi_chinh_quy import SinhVienPhiChinhQuy
from ds_sinh_vien import DanhSachSV

sv1=SinhVienChinhQuy(1987452, "Trần Văn Nghĩa", datetime.strptime("27/2/1999", "%d/%M/%Y"), 80)
sv2=SinhVienChinhQuy(1998745, "Nguyễn Văn Tài", datetime.strptime("2/11/2000", "%d/%M/%Y"), 90)
sv3=SinhVienPhiChinhQuy(1986541, "Vũ Văn Quý", datetime.strptime("16/7/1999", "%d/%M/%Y"), "Cao đẳng", 2)
sv4=SinhVienPhiChinhQuy(1999784, "Tạ Văn Tài", datetime.strptime("2/9/1999", "%d/%M/%Y"), "Cao đẳng", 2)
sv5=SinhVienPhiChinhQuy(2004185, "Trung Hạ Nghĩa", datetime.strptime("27/7/2000", "%d/%M/%Y"), "Trung cấp", 2.5)
sv6=SinhVienChinhQuy(1998745, "Ngô Đặng Nam", datetime.strptime("3/2/2001", "%d/%M/%Y"), 70)
sv7=SinhVienPhiChinhQuy(2015557, "Trần Hạ Thanh", datetime.strptime("8/5/1997", "%d/%M/%Y"), "Cao Đẳng", 3)
sv8=SinhVienChinhQuy(2012254, "Hạ Văn Tùng", datetime.strptime("9/9/1999", "%d/%M/%Y"), 90)

dssv = DanhSachSV()
dssv.them_sv(sv1)
dssv.them_sv(sv2)
dssv.them_sv(sv3)
dssv.them_sv(sv4)
dssv.them_sv(sv5)
dssv.them_sv(sv6)
dssv.them_sv(sv7)
dssv.them_sv(sv8)
dssv.xuat_sv()

ms_can_tim = 2012254
print(f"Sinh viên có mã số {ms_can_tim} ở vị trí {dssv.tim_sv_theo_ms(ms_can_tim)}")

kq = dssv.tim_sv_theo_loai("chinhquy")
print("Danh sách sinh viên theo loại:")
for sv in kq:
    print(sv)

# kq = dssv.tim_diemRL_sv_tren(80)
# print(f"Danh sách sv có điểm trên:")
# for sv in kq:
#     print(sv)