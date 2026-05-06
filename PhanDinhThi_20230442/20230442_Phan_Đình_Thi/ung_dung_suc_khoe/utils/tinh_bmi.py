def tinh_bmi(can_nang, chieu_cao):
    chieu_cao_m = chieu_cao / 100
    return round(can_nang / (chieu_cao_m ** 2), 2)