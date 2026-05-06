from datetime import datetime, timedelta
import calendar
from lunarcalendar import Converter, Solar, Lunar

def get_today():
    """Lấy ngày hôm nay"""
    return datetime.now().date()

def get_lunar_date_vietnam(solar_year, solar_month, solar_day):
    """Chuyển đổi từ lịch dương sang lịch âm Việt Nam (chính xác)"""
    try:
        # Sử dụng thư viện lunarcalendar
        solar = Solar(solar_year, solar_month, solar_day)
        lunar = Converter.Solar2Lunar(solar)
        
        return {
            "year": lunar.year,
            "month": lunar.month,
            "day": lunar.day,
            "is_leap": lunar.isleap
        }
    except Exception as e:
        # Fallback nếu có lỗi
        return {
            "year": solar_year,
            "month": solar_month,
            "day": solar_day,
            "is_leap": False,
            "error": str(e)
        }

def get_lunar_today_vietnam():
    """Lấy ngày âm lịch Việt Nam hôm nay (chính xác)"""
    today = get_today()
    return get_lunar_date_vietnam(today.year, today.month, today.day)

def format_lunar_date_vietnam(lunar_dict):
    """Định dạng ngày âm lịch Việt Nam"""
    if "error" in lunar_dict:
        return "Lỗi chuyển đổi"
    
    leap_str = "nhuận " if lunar_dict.get("is_leap") else ""
    return f"Âm {leap_str}{lunar_dict['month']}/{lunar_dict['day']}/{lunar_dict['year']}"

def get_lunar_zodiac(lunar_month, lunar_day):
    """Lấy con giáp theo lịch âm Việt Nam"""
    zodiacs = [
        "Chuột", "Trâu", "Hổ", "Mèo", "Rồng", "Rắn",
        "Ngựa", "Dê", "Khỉ", "Gà", "Chó", "Lợn"
    ]
    # Con giáp dựa trên tháng âm
    if 1 <= lunar_month <= 12:
        return zodiacs[lunar_month - 1]
    return "N/A"

def get_month_info(year=None, month=None):
    """Lấy thông tin tháng (danh sách ngày)"""
    if year is None:
        year = datetime.now().year
    if month is None:
        month = datetime.now().month
    
    return calendar.monthcalendar(year, month)

def get_days_remaining_in_month():
    """Số ngày còn lại trong tháng"""
    today = get_today()
    last_day = calendar.monthrange(today.year, today.month)[1]
    return last_day - today.day

def get_days_remaining_in_year():
    """Số ngày còn lại trong năm"""
    today = get_today()
    end_of_year = datetime(today.year, 12, 31).date()
    return (end_of_year - today).days

def is_weekend(date_obj=None):
    """Kiểm tra có phải cuối tuần không"""
    if date_obj is None:
        date_obj = get_today()
    return date_obj.weekday() >= 5

def get_week_number():
    """Lấy tuần thứ mấy trong năm"""
    return datetime.now().isocalendar()[1]

def days_until(target_date):
    """Tính ngày còn lại đến ngày chỉ định"""
    today = get_today()
    return (target_date - today).days

def get_zodiac(month, day):
    """Lấy cung hoàng đạo"""
    zodiac_signs = [
        (20, 2, "Bảo Bình"), (21, 3, "Song Ngư"), (21, 4, "Bạch Dương"),
        (20, 5, "Kim Ngưu"), (21, 6, "Song Tử"), (22, 7, "Cự Giải"),
        (23, 8, "Sư Tử"), (23, 9, "Xử Nữ"), (23, 10, "Thiên Bình"),
        (22, 11, "Bọ Cạp"), (22, 12, "Nhân Mã"), (20, 1, "Ma Kết")
    ]
    for sign_day, sign_month, sign_name in zodiac_signs:
        if month == sign_month and day >= sign_day:
            return sign_name
        elif month == (sign_month % 12) + 1 and day < sign_day:
            return zodiac_signs[(zodiac_signs.index((sign_day, sign_month, sign_name)) - 1) % 12][2]
    return None