from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, 
                             QCalendarWidget, QPushButton, QListWidget, QListWidgetItem,
                             QDialog, QLineEdit, QSpinBox, QMessageBox, QDateEdit, QListWidget, QCheckBox)
from PyQt6.QtCore import QTimer, QDate
from core.time_utils import (get_time_by_timezone, get_time_components, 
                             format_time_long, get_timezone_offset, is_daytime,
                             get_multiple_timezones_info)
from core.calendar_utils import get_lunar_today_vietnam, format_lunar_date_vietnam, get_lunar_zodiac
from core.reminder import (load_events, save_event, delete_event, 
                          get_events_by_date, search_events)

class AddEventDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Thêm Sự Kiện")
        self.setGeometry(100, 100, 400, 300)
        
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel("Tiêu đề:"))
        self.title_input = QLineEdit()
        layout.addWidget(self.title_input)
        
        layout.addWidget(QLabel("Ngày:"))
        self.date_edit = QDateEdit()
        self.date_edit.setDate(QDate.currentDate())
        self.date_edit.setCalendarPopup(True)
        layout.addWidget(self.date_edit)
        
        layout.addWidget(QLabel("Thời gian:"))
        time_layout = QHBoxLayout()
        
        time_layout.addWidget(QLabel("Giờ:"))
        self.hour_spin = QSpinBox()
        self.hour_spin.setMinimum(0)
        self.hour_spin.setMaximum(23)
        self.hour_spin.setValue(0)
        time_layout.addWidget(self.hour_spin)
        
        time_layout.addWidget(QLabel("Phút:"))
        self.minute_spin = QSpinBox()
        self.minute_spin.setMinimum(0)
        self.minute_spin.setMaximum(59)
        self.minute_spin.setValue(0)
        time_layout.addWidget(self.minute_spin)
        
        time_layout.addWidget(QLabel("Giây:"))
        self.second_spin = QSpinBox()
        self.second_spin.setMinimum(0)
        self.second_spin.setMaximum(59)
        self.second_spin.setValue(0)
        time_layout.addWidget(self.second_spin)
        
        layout.addLayout(time_layout)
        
        btn_layout = QHBoxLayout()
        ok_btn = QPushButton("OK")
        cancel_btn = QPushButton("Hủy")
        ok_btn.clicked.connect(self.accept)
        cancel_btn.clicked.connect(self.reject)
        btn_layout.addWidget(ok_btn)
        btn_layout.addWidget(cancel_btn)
        layout.addLayout(btn_layout)
        
        self.setLayout(layout)
    
    def get_data(self):
        date_str = self.date_edit.date().toString("yyyy-MM-dd")
        time_str = f"{self.hour_spin.value():02d}:{self.minute_spin.value():02d}"
        return {
            "title": self.title_input.text(),
            "time": f"{date_str} {time_str}"
        }

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("App Đồng Hồ Của Thi")
        self.setGeometry(100, 100, 900, 700)
        self.selected_date = None

        main_layout = QHBoxLayout()

        # Left panel: Thời gian
        left_layout = QVBoxLayout()
        
        left_layout.addWidget(QLabel("Múi giờ:"))
        self.combo = QComboBox()
        self.combo.addItems([
            "Asia/Ho_Chi_Minh",
            "Asia/Bangkok",
            "Asia/Tokyo",
            "Asia/Seoul",
            "Asia/Shanghai",
            "Asia/Kolkata",
            "Europe/London",
            "Europe/Paris",
            "Europe/Berlin",
            "America/New_York",
            "America/Chicago",
            "America/Los_Angeles",
            "Australia/Sydney"
        ])
        self.combo.currentTextChanged.connect(self.on_timezone_changed)
        left_layout.addWidget(self.combo)
        

        left_layout.addWidget(QLabel("Thời gian:"))
        self.label_long = QLabel()
        self.label_long.setStyleSheet("font-size: 12px; font-weight: bold;")
        left_layout.addWidget(self.label_long)

        left_layout.addWidget(QLabel("Offset múi giờ:"))
        self.label_offset = QLabel()
        left_layout.addWidget(self.label_offset)

        left_layout.addWidget(QLabel("Trạng thái:"))
        self.label_daytime = QLabel()
        left_layout.addWidget(self.label_daytime)

        left_layout.addWidget(QLabel("Lịch âm:"))
        self.label_lunar = QLabel()
        self.label_lunar.setStyleSheet("font-size: 12px; color: blue;")
        left_layout.addWidget(self.label_lunar)

        # Chọn múi giờ để so sánh
        left_layout.addWidget(QLabel("So sánh múi giờ:"))
        self.comparison_combo = QComboBox()
        self.comparison_combo.addItems([
            "Không chọn",
            "Asia/Ho_Chi_Minh",
            "Asia/Bangkok",
            "Asia/Tokyo",
            "Asia/Seoul",
            "Asia/Shanghai",
            "Asia/Kolkata",
            "Europe/London",
            "Europe/Paris",
            "Europe/Berlin",
            "America/New_York",
            "America/Chicago",
            "America/Los_Angeles",
            "Australia/Sydney"
        ])
        self.comparison_combo.currentTextChanged.connect(self.update_comparison)
        left_layout.addWidget(self.comparison_combo)

        self.label_comparison = QLabel()
        self.label_comparison.setStyleSheet("font-size: 10px; background-color: black; color: white; padding: 5px;")
        left_layout.addWidget(self.label_comparison)

        left_layout.addStretch()

        # Right panel: Lịch & Sự kiện
        right_layout = QVBoxLayout()

        right_layout.addWidget(QLabel("Lịch:"))
        self.calendar = QCalendarWidget()
        self.calendar.clicked.connect(self.on_calendar_clicked)
        right_layout.addWidget(self.calendar)

        right_layout.addWidget(QLabel("Báo Thức & Sự Kiện:"))
        self.event_list = QListWidget()
        right_layout.addWidget(self.event_list)

        btn_layout = QHBoxLayout()
        btn_add = QPushButton("Thêm")
        btn_delete = QPushButton("Xóa")
        btn_refresh = QPushButton("Làm mới")
        btn_add.clicked.connect(self.add_event)
        btn_delete.clicked.connect(self.delete_selected_event)
        btn_refresh.clicked.connect(self.refresh_events)
        btn_layout.addWidget(btn_add)
        btn_layout.addWidget(btn_delete)
        btn_layout.addWidget(btn_refresh)
        right_layout.addLayout(btn_layout)

        main_layout.addLayout(left_layout, 1)
        main_layout.addLayout(right_layout, 1)
        self.setLayout(main_layout)

        # Timer để cập nhật thời gian
        timer = QTimer(self)
        timer.timeout.connect(self.update_time)
        timer.start(1000)
        
        # Timer để kiểm tra sự kiện mỗi phút
        event_timer = QTimer(self)
        event_timer.timeout.connect(self.check_events_notification)
        event_timer.start(60000) 
        
        self.update_time()
        self.refresh_events()

    def update_time(self):
        tz = self.combo.currentText()
        self.label_long.setText(format_time_long(tz))
        
        offset = get_timezone_offset(tz)
        self.label_offset.setText(offset if offset else "N/A")
        
        status = "☀️ Ban ngày" if is_daytime(tz) else "🌙 Ban đêm"
        self.label_daytime.setText(status)
        
        # Cập nhật lịch âm Việt Nam
        lunar = get_lunar_today_vietnam()
        lunar_str = format_lunar_date_vietnam(lunar)
        zodiac = get_lunar_zodiac(lunar.get("month"), lunar.get("day")) if "error" not in lunar else "N/A"
        self.label_lunar.setText(f"{lunar_str} ({zodiac})")
        
        # Cập nhật so sánh múi giờ
        self.update_comparison()

    def update_comparison(self):
        """Hiển thị so sánh múi giờ"""
        selected = self.comparison_combo.currentText()
        
        if selected == "Không chọn":
            self.label_comparison.setText("")
            return
        
        tz_main = self.combo.currentText()
        info = get_multiple_timezones_info([tz_main, selected])
        
        main_info = info[tz_main]
        comp_info = info[selected]
        
        text = f"{tz_main}:\n{main_info['time']} ({main_info['offset']})\n\n"
        text += f"{selected}:\n{comp_info['time']} ({comp_info['offset']})"
        
        self.label_comparison.setText(text)

    def on_timezone_changed(self):
        self.update_time()
        self.update_comparison()

    def on_calendar_clicked(self, date):
        self.selected_date = date.toString("yyyy-MM-dd")
        self.refresh_events()

    def refresh_events(self):
        self.event_list.clear()
        date_str = self.selected_date or self.calendar.selectedDate().toString("yyyy-MM-dd")
        events = get_events_by_date(date_str)
        
        for event in events:
            item_text = f"{event.get('time', '')} - {event.get('title', '')}"
            item = QListWidgetItem(item_text)
            item.setData(1, event.get("id"))
            self.event_list.addItem(item)

    def add_event(self):
        dialog = AddEventDialog(self)
        if dialog.exec():
            data = dialog.get_data()
            if data["title"] and data["time"]:
                try:
                    save_event(data)
                    self.refresh_events()
                    QMessageBox.information(self, "Thành công", "Sự kiện đã được thêm!")
                except Exception as e:
                    QMessageBox.warning(self, "Lỗi", f"Không thể thêm sự kiện: {str(e)}")

    def delete_selected_event(self):
        current_item = self.event_list.currentItem()
        if current_item:
            event_id = current_item.data(1)
            delete_event(event_id)
            self.refresh_events()
            QMessageBox.information(self, "Thành công", "Sự kiện đã được xóa!")

    def check_events_notification(self):
        """Kiểm tra sự kiện và hiển thị thông báo"""
        from datetime import datetime
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M")
        
        events = load_events()
        for event in events:
            event_time = event.get("time", "")
            if event_time == current_time:
                title = event.get("title", "Sự kiện")
                QMessageBox.warning(
                    self, 
                    "THÔNG BÁO SỰ KIỆN", 
                    f"Đã đến giờ:\n\n{title}\n\nThời gian: {event_time}"
                )