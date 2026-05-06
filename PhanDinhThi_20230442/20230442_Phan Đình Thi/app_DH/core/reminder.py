import json
import os
from datetime import datetime

FILE = "data/events.json"

def ensure_data_dir():
    """Tạo thư mục data nếu chưa tồn tại"""
    os.makedirs("data", exist_ok=True)
    if not os.path.exists(FILE):
        with open(FILE, "w") as f:
            json.dump([], f, indent=4)

def load_events():
    ensure_data_dir()
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_event(event):
    """Thêm sự kiện mới"""
    ensure_data_dir()
    events = load_events()
    event["id"] = len(events) + 1
    events.append(event)
    with open(FILE, "w") as f:
        json.dump(events, f, indent=4, ensure_ascii=False)
    return event

def delete_event(event_id):
    """Xóa sự kiện theo ID"""
    ensure_data_dir()
    events = load_events()
    events = [e for e in events if e.get("id") != event_id]
    with open(FILE, "w") as f:
        json.dump(events, f, indent=4, ensure_ascii=False)

def update_event(event_id, updated_data):
    """Chỉnh sửa sự kiện"""
    ensure_data_dir()
    events = load_events()
    for e in events:
        if e.get("id") == event_id:
            e.update(updated_data)
            break
    with open(FILE, "w") as f:
        json.dump(events, f, indent=4, ensure_ascii=False)

def get_event(event_id):
    """Lấy thông tin một sự kiện"""
    ensure_data_dir()
    events = load_events()
    for e in events:
        if e.get("id") == event_id:
            return e
    return None

def search_events(keyword):
    """Tìm kiếm sự kiện theo từ khóa"""
    ensure_data_dir()
    events = load_events()
    return [e for e in events if keyword.lower() in e.get("title", "").lower()]

def get_events_by_date(date_str):
    """Lấy sự kiện theo ngày (định dạng YYYY-MM-DD)"""
    ensure_data_dir()
    events = load_events()
    return [e for e in events if e.get("time", "").startswith(date_str)]

def check_events():
    """Kiểm tra sự kiện sắp tới"""
    ensure_data_dir()
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    events = load_events()

    for e in events:
        if e.get("time") == now:
            print("🔔 Nhắc:", e.get("title", "No title"))

def get_upcoming_events(hours=24):
    """Lấy sự kiện sắp tới trong N giờ"""
    ensure_data_dir()
    events = load_events()
    now = datetime.now()
    upcoming = []
    
    for e in events:
        try:
            event_time = datetime.strptime(e.get("time", ""), "%Y-%m-%d %H:%M")
            if now <= event_time <= now.replace(hour=(now.hour + hours) % 24):
                upcoming.append(e)
        except:
            pass
    
    return sorted(upcoming, key=lambda x: x.get("time", ""))

def clear_expired_events():
    """Xóa sự kiện đã qua"""
    ensure_data_dir()
    events = load_events()
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    events = [e for e in events if e.get("time", "") >= now]
    with open(FILE, "w") as f:
        json.dump(events, f, indent=4, ensure_ascii=False)