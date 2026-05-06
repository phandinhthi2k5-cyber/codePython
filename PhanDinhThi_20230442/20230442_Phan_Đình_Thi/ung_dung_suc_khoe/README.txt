
CÀI ĐẶT CÁC THƯ VIỆN 

Cài đặt một lần:
    pip install pyqt6 pandas matplotlib

Chi tiết các gói:
    • PyQt6         - Thư viện tạo giao diện người dùng (GUI)
    • pandas        - Xử lý và lưu trữ dữ liệu CSV
    • matplotlib    - Vẽ biểu đồ và đồ thị
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CÁCH CHẠY ỨNG DỤNG

    python main.py

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
điều kiện
BMI (Chỉ số khối cơ thể):
    Thiếu cân:  < 18.5
    Bình thường: 18.5 - 25
    Thừa cân:   25 - 30
    Béo phì:    > 30

Nhịp tim (bpm):
    Thấp:       < 60
    Bình thường: 60 - 100
    Cao:        100 - 120
    Nguy hiểm:  > 120

SpO2 (%) - Độ bão hòa oxy:
    Nguy hiểm:  < 90
    Thấp:       90 - 95
    Bình thường: ≥ 95

CO2 (ppm) - Nồng độ khí CO2:
    Thấp:       < 20
    Bình thường: 20 - 40
    Cao:        40 - 50
    Nguy hiểm:  > 50

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Dữ liệu được lưu tự động vào file: data/suc_khoe.csv

Cột dữ liệu:
    • thoi_gian:  Ngày giờ kiểm tra (YYYY-MM-DD HH:MM)
    • can_nang:   Cân nặng (kg)
    • chieu_cao:  Chiều cao (cm)
    • bmi:        Chỉ số BMI
    • nhip_tim:   Nhịp tim (bpm)
    • spo2:       Độ bão hòa oxy (%)
    • co2:        Nồng độ CO2 (ppm)
