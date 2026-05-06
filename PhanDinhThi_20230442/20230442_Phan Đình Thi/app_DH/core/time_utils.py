from datetime import datetime, timedelta
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

def get_time_by_timezone(tz_name):
    try:
        tz = ZoneInfo(tz_name)
    except ZoneInfoNotFoundError:
        tz = None

    now = datetime.now(tz) if tz else datetime.now()
    if tz:
        return now.strftime("%Y-%m-%d %H:%M:%S")
    return f"{now.strftime('%Y-%m-%d %H:%M:%S')} (local)"

def get_time_components(tz_name):
    """Trả về các thành phần riêng biệt của thời gian"""
    try:
        tz = ZoneInfo(tz_name)
    except ZoneInfoNotFoundError:
        tz = None
    
    now = datetime.now(tz) if tz else datetime.now()
    return {
        "date": now.strftime("%d/%m/%Y"),
        "time": now.strftime("%H:%M:%S"),
        "day": now.strftime("%A"),
        "hour": now.hour,
        "minute": now.minute,
        "second": now.second
    }

def format_time_long(tz_name):
    """Định dạng dài: Thứ, DD/MM/YYYY HH:MM:SS"""
    try:
        tz = ZoneInfo(tz_name)
    except ZoneInfoNotFoundError:
        tz = None
    
    now = datetime.now(tz) if tz else datetime.now()
    day_map = {
        "Monday": "Thứ 2",
        "Tuesday": "Thứ 3",
        "Wednesday": "Thứ 4",
        "Thursday": "Thứ 5",
        "Friday": "Thứ 6",
        "Saturday": "Thứ 7",
        "Sunday": "Chủ nhật"
    }
    day_name = day_map.get(now.strftime("%A"), now.strftime("%A"))
    return f"{day_name}, {now.strftime('%d/%m/%Y %H:%M:%S')}"

def get_timezone_offset(tz_name):
    """Lấy offset của múi giờ so với UTC"""
    try:
        tz = ZoneInfo(tz_name)
    except ZoneInfoNotFoundError:
        return None
    
    now = datetime.now(tz)
    offset = now.strftime("%z")
    return f"UTC{offset[:3]}:{offset[3:]}"

def is_daytime(tz_name):
    """Kiểm tra có phải ban ngày không (6:00 - 18:00)"""
    try:
        tz = ZoneInfo(tz_name)
    except ZoneInfoNotFoundError:
        tz = None
    
    now = datetime.now(tz) if tz else datetime.now()
    return 6 <= now.hour < 18

def get_multiple_timezones_info(tz_list):
    """Lấy thông tin thời gian của nhiều múi giờ"""
    result = {}
    for tz_name in tz_list:
        try:
            tz = ZoneInfo(tz_name)
        except ZoneInfoNotFoundError:
            tz = None
        
        now = datetime.now(tz) if tz else datetime.now()
        offset = now.strftime("%z")
        offset_str = f"UTC{offset[:3]}:{offset[3:]}" if offset else "N/A"
        
        result[tz_name] = {
            "time": now.strftime("%H:%M:%S"),
            "date": now.strftime("%d/%m/%Y"),
            "offset": offset_str,
            "day": now.strftime("%A")
        }
    
    return result