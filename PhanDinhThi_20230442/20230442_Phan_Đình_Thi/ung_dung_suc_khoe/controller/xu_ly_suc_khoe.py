from model.du_lieu_suc_khoe import DuLieuSucKhoe
from model.phan_tich_suc_khoe import PhanTichSucKhoe
from utils.tinh_bmi import tinh_bmi
from utils.kiem_tra_du_lieu import hop_le

class XuLySucKhoe:
    def __init__(self, view):
        self.view = view
        self.model = DuLieuSucKhoe()

        self.view.btn_luu.clicked.connect(self.luu_du_lieu)
        self.view.btn_thong_ke.clicked.connect(self.hien_thi_bieu_do)
        self.view.btn_lam_moi.clicked.connect(self.view.lam_moi)
        self.view.btn_lich_su.clicked.connect(self.xem_lich_su)

    def luu_du_lieu(self):
        cn = self.view.input_can_nang.text()
        cc = self.view.input_chieu_cao.text()
        nt = self.view.input_nhip_tim.text()
        spo2 = self.view.input_spo2.text()
        co2 = self.view.input_co2.text()

        hop_le_check, mess = hop_le(cn, cc, nt, spo2, co2)
        if not hop_le_check:
            self.view.hien_thi("❌ LỖI: " + mess)
            return
        
        cn, cc, nt, spo2, co2 = float(cn), float(cc), int(nt), int(spo2), float(co2)

        bmi = tinh_bmi(cn, cc)
        self.model.luu(cn, cc, bmi, nt, spo2, co2)

        chi_tiet = PhanTichSucKhoe.kiem_tra(bmi, nt, spo2, co2)

        # Tạo thông báo chi tiết
        thong_bao = "=" * 60 + "\n"
        thong_bao += "KẾT QUẢ KIỂM TRA SỨC KHỎE\n"
        thong_bao += "=" * 60 + "\n\n"
        
        # Thông tin chỉ số
        thong_bao += "CÁC CHỈ SỐ:\n"
        thong_bao += f"  • Cân nặng: {cn} kg\n"
        thong_bao += f"  • Chiều cao: {cc} cm\n"
        thong_bao += f"  • BMI: {bmi}\n"
        thong_bao += f"  • Nhịp tim: {nt} bpm\n"
        thong_bao += f"  • SpO2: {spo2} %\n"
        thong_bao += f"  • CO2: {co2} ppm\n\n"
        
        # Tổng hợp
        thong_bao += "ĐÁNH GIÁ TỔNG HỢP:\n"
        for item in chi_tiet["tong_hop"]:
            thong_bao += f"  • {item}\n"
        thong_bao += "\n"
        
        # Cảnh báo (nếu có)
        if chi_tiet["canh_bao"]:
            thong_bao += "CẢNH BÁO:\n"
            for canh in chi_tiet["canh_bao"]:
                thong_bao += f"  {canh}\n"
            thong_bao += "\n"
        
        # Lời khuyên
        if chi_tiet["loi_khuyen"]:
            thong_bao += "LỜI KHUYÊN:\n"
            for khuyen in chi_tiet["loi_khuyen"]:
                thong_bao += f"  {khuyen}\n"
        
        thong_bao += "\n" + "=" * 60
        
        self.view.hien_thi(thong_bao)
        
        # Xóa input
        self.view.input_can_nang.clear()
        self.view.input_chieu_cao.clear()
        self.view.input_nhip_tim.clear()
        self.view.input_spo2.clear()
        self.view.input_co2.clear()

    def hien_thi_bieu_do(self):
        df = self.model.doc()
        if df.empty:
            self.view.hien_thi("❌ Không có dữ liệu để hiển thị")
            return
        
        # Hiển thị thống kê
        thong_ke = PhanTichSucKhoe.thong_ke(df)
        self.view.hien_thi_thong_ke(thong_ke)
        self.view.ve_bieu_do(df)

    def xem_lich_su(self):
        df = self.model.doc()
        self.view.xem_lich_su(df)
