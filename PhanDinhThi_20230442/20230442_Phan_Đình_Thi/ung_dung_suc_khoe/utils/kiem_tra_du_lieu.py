def hop_le(can_nang, chieu_cao, nhip_tim, spo2, co2):
    try:
        can_nang = float(can_nang)
        chieu_cao = float(chieu_cao)
        nhip_tim = int(nhip_tim)
        spo2 = int(spo2)
        co2 = float(co2)
        
        # Kiểm tra giá trị hợp lệ
        if can_nang <= 0 or can_nang > 200:
            return False, "Cân nặng không hợp lệ (1-200 kg)"
        if chieu_cao <= 0 or chieu_cao > 300:
            return False, "Chiều cao không hợp lệ (1-300 cm)"
        if nhip_tim < 0 or nhip_tim > 200:
            return False, "Nhịp tim không hợp lệ (0-200)"
        if spo2 < 0 or spo2 > 100:
            return False, "SpO2 không hợp lệ (0-100)"
        if co2 < 0 or co2 > 100:
            return False, "CO2 không hợp lệ (0-100)"
        
        return True, "Hợp lệ"
    except ValueError:
        return False, "Vui lòng nhập số"