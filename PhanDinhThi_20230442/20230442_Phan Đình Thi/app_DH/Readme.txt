
CÁC THƯ VIỆN ĐÃ CÀI ĐẶT (REQUIREMENTS.TXT)

1. PyQt6 - Thư viện tạo giao diện GUI
   - Phiên bản: Latest
   - Tác dụng: Tạo cửa sổ ứng dụng, các widget (nút, nhãn, combo box, lịch, etc.)
   - Import: from PyQt6.QtWidgets, from PyQt6.QtCore

2. tzdata - Dữ liệu múi giờ toàn thế giới
   - Phiên bản: Latest
   - Tác dụng: Cung cấp thông tin múi giờ để zoneinfo.ZoneInfo hoạt động
   - Tại sao cần: Để chương trình có thể nhận diện múi giờ như "Asia/Ho_Chi_Minh", "America/New_York"

3. lunarcalendar - Thư viện lịch âm chính xác
   - Phiên bản: Latest
   - Tác dụng: Chuyển đổi chính xác từ lịch dương sang lịch âm Việt Nam
   - Tại sao cần: Để hiển thị lịch âm Việt Nam chính xác và con giáp


CÁC THƯ VIỆN BUILT-IN

1. sys - Xử lý tham số hệ thống
   - Dùng: sys.exit() để thoát ứng dụng

2. datetime - Xử lý ngày, giờ, thời gian
   - Dùng: Lấy thời gian hiện tại, định dạng thời gian

3. zoneinfo - Quản lý múi giờ (Python 3.9+)
   - Dùng: ZoneInfo() để chuyển đổi thời gian giữa các múi giờ

4. calendar - Xử lý lịch
   - Dùng: Lấy thông tin tháng, tuần, kiểm tra ngày

5. json - Xử lý dữ liệu JSON
   - Dùng: Lưu/đọc sự kiện từ file events.json


CẤU TRÚC DỰ ÁN

app_DH/
├── main.py                 - Điểm vào ứng dụng
├── requirements.txt        - Danh sách thư viện cần cài
├── Readme.txt             - Tài liệu này
│
├── core/                   - Hạt nhân logic ứng dụng
│   ├── time_utils.py      - Hàm xử lý thời gian & múi giờ
│   ├── calendar_utils.py  - Hàm xử lý lịch
│   └── reminder.py        - Hàm quản lý sự kiện
│
├── ui/                     - Giao diện người dùng
│   └── main_window.py     - Cửa sổ chính & dialog
│
└── data/                   - Dữ liệu
    ├── events.json        - Lưu danh sách sự kiện
    └── config.json        - Tệp cấu hình (dự phòng)

CÁC CHỨC NĂNG CHÍNH

1️    HIỂN THỊ THỜI GIAN
   ✓ Hiển thị thời gian real-time (cập nhật mỗi giây)
   ✓ Hỗ trợ 13 múi giờ: Asia/Ho_Chi_Minh, Asia/Tokyo, America/New_York, etc.
   ✓ Hiển thị format ngắn: YYYY-MM-DD HH:MM:SS
   ✓ Hiển thị format dài: Thứ X, DD/MM/YYYY HH:MM:SS
   ✓ Hiển thị offset so với UTC
   ✓ Trạng thái ban ngày/đêm (☀️/🌙)

2️    HIỂN THỊ LỊCH
   ✓ Widget lịch tương tác
   ✓ Click trên ngày để xem sự kiện của ngày đó
   ✓ Lịch âm Việt Nam chính xác (dựa trên lunarcalendar)
   ✓ Hiển thị con giáp theo tháng âm
   ✓ So sánh múi giờ khác nhau (chọn múi giờ để xem giờ tương ứng)

3️   QUẢN LÝ SỰ KIỆN
   ✓ Thêm sự kiện mới (dialog nhập tiêu đề, ngày, giờ)
   ✓ Xóa sự kiện
   ✓ Hiển thị danh sách sự kiện
   ✓ Tìm kiếm sự kiện
   ✓ Lưu trữ trong file JSON

HƯỚNG DẪN CHẠY CHƯƠNG TRÌNH
1. Cài đặt dependencies:
   pip install -r requirements.txt
2. Chạy ứng dụng:
   python main.py
   Hoặc từ thư mục gốc project:
   d:/Python/PhanDinhThi_20230442/.venv/Scripts/python.exe d:/Python/PhanDinhThi_20230442/app_DH/main.py
3. Sử dụng:
   - Chọn múi giờ từ dropdown (combo box)
   - Xem thời gian cập nhật real-time
   - Click trên lịch để xem/thêm sự kiện
   - Nhấn "Thêm" để tạo sự kiện mới
   - Nhấn "Xóa" để xóa sự kiện đã chọn