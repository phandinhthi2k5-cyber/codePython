class PhanTichSucKhoe:

    @staticmethod
    def kiem_tra(bmi, nhip_tim, spo2, co2):
        chi_tiet = {
            "canh_bao": [],
            "tong_hop": [],
            "loi_khuyen": [],
            "muc_do": 0
        }

        # Kiểm tra BMI
        if bmi < 18.5:
            chi_tiet["canh_bao"].append("hiếu cân (BMI: " + str(bmi) + ")")
            chi_tiet["tong_hop"].append("BMI < 18.5 - THIẾU CÂN")
            chi_tiet["loi_khuyen"].append("BMI: Tăng cân bằng cách ăn uống cân bằng, tập thể dục phù hợp. Tham khảo bác sĩ dinh dưỡng.")
            chi_tiet["muc_do"] += 1
        elif bmi > 25:
            if bmi > 30:
                chi_tiet["canh_bao"].append("BÉO PHÌ (BMI: " + str(bmi) + ")")
                chi_tiet["tong_hop"].append("BMI > 30 - BÉO PHÌ (NGUY HIỂM)")
                chi_tiet["loi_khuyen"].append("BMI: HÀNH ĐỘNG NGAY - Giảm cân theo hướng dẫn của bác sĩ. Tập luyện thường xuyên, kiểm soát chế độ ăn uống.")
                chi_tiet["muc_do"] += 2
            else:
                chi_tiet["canh_bao"].append("Thừa cân (BMI: " + str(bmi) + ")")
                chi_tiet["tong_hop"].append("25 < BMI < 30 - THỪA CÂN")
                chi_tiet["loi_khuyen"].append("BMI: Giảm cân từ từ qua tập thể dục và ăn uống lành mạnh.")
                chi_tiet["muc_do"] += 1
        else:
            chi_tiet["tong_hop"].append("BMI: " + str(bmi) + " - BÌNH THƯỜNG")

        # Kiểm tra nhịp tim
        if nhip_tim < 60:
            chi_tiet["canh_bao"].append("Nhịp tim thấp: " + str(nhip_tim) + " bpm")
            chi_tiet["tong_hop"].append("Nhịp tim < 60 - THẤP")
            chi_tiet["loi_khuyen"].append("Nhịp tim: Nghỉ ngơi, tránh căng thẳng. Nếu kéo dài, liên hệ bác sĩ.")
            chi_tiet["muc_do"] += 1
        elif nhip_tim > 100:
            if nhip_tim > 120:
                chi_tiet["canh_bao"].append("Nhịp tim CAO: " + str(nhip_tim) + " bpm")
                chi_tiet["tong_hop"].append("Nhịp tim > 120 - CAO (NGUY HIỂM)")
                chi_tiet["loi_khuyen"].append("Nhịp tim: HÃY GỌI CẤP CỨU - Ngồi, thở từ từ. Cần kiểm tra y tế ngay!")
                chi_tiet["muc_do"] += 2
            else:
                chi_tiet["canh_bao"].append("Nhịp tim cao: " + str(nhip_tim) + " bpm")
                chi_tiet["tong_hop"].append("100 < Nhịp tim < 120 - CAO")
                chi_tiet["loi_khuyen"].append("Nhịp tim: Thả lỏng, kiểm soát stress. Tránh caffeine, rượu.")
                chi_tiet["muc_do"] += 1
        else:
            chi_tiet["tong_hop"].append("Nhịp tim: " + str(nhip_tim) + " bpm - BÌNH THƯỜNG")

        # Kiểm tra SpO2
        if spo2 < 90:
            chi_tiet["canh_bao"].append("SpO2 NGUY HIỂM: " + str(spo2) + "%")
            chi_tiet["tong_hop"].append("SpO2 < 90% - NGUY HIỂM")
            chi_tiet["loi_khuyen"].append("SpO2: HÃY GỌI CẤP CỨU - Bệnh nhân cần oxy. Đây là tình trạng cấp cứu!")
            chi_tiet["muc_do"] += 2
        elif spo2 < 95:
            chi_tiet["canh_bao"].append("SpO2 thấp: " + str(spo2) + "%")
            chi_tiet["tong_hop"].append("90% ≤ SpO2 < 95% - THẤP")
            chi_tiet["loi_khuyen"].append("SpO2: Thở sâu, tránh hoạt động nặng. Cần hỗ trợ oxy, liên hệ bác sĩ.")
            chi_tiet["muc_do"] += 1
        else:
            chi_tiet["tong_hop"].append("SpO2: " + str(spo2) + "% - BÌNH THƯỜNG")

        # Kiểm tra CO2
        if co2 > 50:
            chi_tiet["canh_bao"].append("CO2 CAO: " + str(co2) + " ppm")
            chi_tiet["tong_hop"].append("CO2 > 50 ppm - CAO (NGUY HIỂM)")
            chi_tiet["loi_khuyen"].append("CO2: NGUY HIỂM - Cần thông khí tốt, tập thở. Liên hệ bác sĩ ngay!")
            chi_tiet["muc_do"] += 2
        elif co2 > 40:
            chi_tiet["canh_bao"].append("CO2 cao: " + str(co2) + " ppm")
            chi_tiet["tong_hop"].append("40 < CO2 < 50 ppm - CAO")
            chi_tiet["loi_khuyen"].append("CO2: Tăng thông khí, mở cửa sổ. Tập các bài thở sâu.")
            chi_tiet["muc_do"] += 1
        elif co2 < 20:
            chi_tiet["canh_bao"].append("CO2 thấp: " + str(co2) + " ppm")
            chi_tiet["tong_hop"].append("CO2 < 20 ppm - THẤP")
            chi_tiet["loi_khuyen"].append("CO2: Thở bình thường, không thở quá sâu. Thả lỏng căng thẳng.")
            chi_tiet["muc_do"] += 1
        else:
            chi_tiet["tong_hop"].append("CO2: " + str(co2) + " ppm - BÌNH THƯỜNG")

        return chi_tiet
    
    @staticmethod
    def thong_ke(df):
        if df.empty:
            return {}
        
        return {
            "tong_lan_kiem_tra": len(df),
            "bmi_tb": round(df["bmi"].mean(), 2),
            "nhip_tim_tb": round(df["nhip_tim"].mean(), 0),
            "spo2_tb": round(df["spo2"].mean(), 1),
            "co2_tb": round(df["co2"].mean(), 2),
            "bmi_min": round(df["bmi"].min(), 2),
            "bmi_max": round(df["bmi"].max(), 2),
            "nhip_tim_min": df["nhip_tim"].min(),
            "nhip_tim_max": df["nhip_tim"].max(),
            "spo2_min": df["spo2"].min(),
            "spo2_max": df["spo2"].max(),
            "co2_min": round(df["co2"].min(), 2),
            "co2_max": round(df["co2"].max(), 2)
        }
    
    @staticmethod
    def thong_ke(df):
        if df.empty:
            return {}
        
        return {
            "tong_lan_kiem_tra": len(df),
            "bmi_tb": round(df["bmi"].mean(), 2),
            "nhip_tim_tb": round(df["nhip_tim"].mean(), 0),
            "spo2_tb": round(df["spo2"].mean(), 1),
            "co2_tb": round(df["co2"].mean(), 2),
            "bmi_min": round(df["bmi"].min(), 2),
            "bmi_max": round(df["bmi"].max(), 2),
            "nhip_tim_min": df["nhip_tim"].min(),
            "nhip_tim_max": df["nhip_tim"].max(),
            "spo2_min": df["spo2"].min(),
            "spo2_max": df["spo2"].max(),
            "co2_min": round(df["co2"].min(), 2),
            "co2_max": round(df["co2"].max(), 2)
        }