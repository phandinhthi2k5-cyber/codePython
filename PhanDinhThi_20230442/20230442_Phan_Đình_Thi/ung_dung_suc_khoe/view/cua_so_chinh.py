from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, 
                             QLineEdit, QGroupBox, QScrollArea, QFrame, QSizePolicy,
                             QDialog, QTableWidget, QTableWidgetItem, QHeaderView)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QColor
from view.bieu_do import BieuDo

class CuaSoChinh(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ứng dụng Quản lý Sức Khỏe")
        self.setGeometry(100, 100, 1000, 800)

        main_layout = QHBoxLayout()

        # Bên trái: Input form
        left_layout = QVBoxLayout()
        left_widget = QWidget()
        
        # Title
        title = QLabel("NHẬP CHỈ SỐ SỨC KHỎE")
        title_font = QFont()
        title_font.setBold(True)
        title_font.setPointSize(12)
        title.setFont(title_font)
        left_layout.addWidget(title)

        # Input group
        input_group = QGroupBox("Thông tin sức khỏe")
        input_layout = QVBoxLayout()

        self.input_can_nang = QLineEdit()
        self.input_can_nang.setPlaceholderText("Cân nặng (kg)")
        
        self.input_chieu_cao = QLineEdit()
        self.input_chieu_cao.setPlaceholderText("Chiều cao (cm)")
        
        self.input_nhip_tim = QLineEdit()
        self.input_nhip_tim.setPlaceholderText("Nhịp tim (bpm)")
        
        self.input_spo2 = QLineEdit()
        self.input_spo2.setPlaceholderText("SpO2 (%)")
        
        self.input_co2 = QLineEdit()
        self.input_co2.setPlaceholderText("CO2 (ppm)")

        input_layout.addWidget(self.input_can_nang)
        input_layout.addWidget(self.input_chieu_cao)
        input_layout.addWidget(self.input_nhip_tim)
        input_layout.addWidget(self.input_spo2)
        input_layout.addWidget(self.input_co2)
        input_group.setLayout(input_layout)
        left_layout.addWidget(input_group)

        # Buttons
        button_layout = QHBoxLayout()
        self.btn_luu = QPushButton("Xem và Lưu")
        self.btn_luu.setMinimumHeight(40)
        self.btn_luu.setStyleSheet("background-color: green; color: white; font-weight: bold;")
        
        self.btn_thong_ke = QPushButton("Xem thống kê")
        self.btn_thong_ke.setMinimumHeight(40)
        self.btn_thong_ke.setStyleSheet("background-color: green; color: white; font-weight: bold;")
        
        self.btn_lam_moi = QPushButton("Làm mới")
        self.btn_lam_moi.setMinimumHeight(40)
        self.btn_lam_moi.setStyleSheet("background-color: green; color: white; font-weight: bold;")
        
        self.btn_lich_su = QPushButton("Xem lịch sử")
        self.btn_lich_su.setMinimumHeight(40)
        self.btn_lich_su.setStyleSheet("background-color: #FF9800; color: white; font-weight: bold;")
        
        button_layout.addWidget(self.btn_luu)
        button_layout.addWidget(self.btn_thong_ke)
        button_layout.addWidget(self.btn_lam_moi)
        button_layout.addWidget(self.btn_lich_su)
        left_layout.addLayout(button_layout)

        # Status/Message
        self.label = QLabel("")
        self.label.setWordWrap(True)
        self.label.setMinimumHeight(100)
        status_group = QGroupBox("Thông báo")
        status_layout = QVBoxLayout()
        status_layout.addWidget(self.label)
        status_group.setLayout(status_layout)
        left_layout.addWidget(status_group)

        # Statistics
        self.label_thong_ke = QLabel("")
        self.label_thong_ke.setWordWrap(True)
        self.label_thong_ke.setMinimumHeight(150)
        stat_group = QGroupBox("Thống kê tổng quát")
        stat_layout = QVBoxLayout()
        stat_layout.addWidget(self.label_thong_ke)
        stat_group.setLayout(stat_layout)
        left_layout.addWidget(stat_group)

        left_layout.addStretch()
        left_widget.setLayout(left_layout)
        
        scroll = QScrollArea()
        scroll.setWidget(left_widget)
        scroll.setWidgetResizable(True)
        main_layout.addWidget(scroll, 1)

        # Bên phải: Chart
        right_layout = QVBoxLayout()
        chart_label = QLabel("BIỂU ĐỒ THEO DÕI")
        chart_label.setFont(title_font)
        chart_label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        chart_label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        right_layout.addWidget(chart_label)
        
        self.bieu_do = BieuDo()
        self.bieu_do.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        right_layout.addWidget(self.bieu_do, 1)
        
        main_layout.addLayout(right_layout, 2)

        self.setLayout(main_layout)

    def hien_thi(self, text):
        self.label.setText(text)

    def hien_thi_thong_ke(self, thong_ke):
        if not thong_ke:
            self.label_thong_ke.setText("Chưa có dữ liệu")
            return
        
        text = f"""
        📈 THỐNG KÊ TỔNG HỢP:
        
        Số lần kiểm tra: {thong_ke.get('tong_lan_kiem_tra', 0)}
        
        BMI:
          • Trung bình: {thong_ke.get('bmi_tb', 0)}
          • Min: {thong_ke.get('bmi_min', 0)} | Max: {thong_ke.get('bmi_max', 0)}
        
        Nhịp tim (bpm):
          • Trung bình: {int(thong_ke.get('nhip_tim_tb', 0))}
          • Min: {thong_ke.get('nhip_tim_min', 0)} | Max: {thong_ke.get('nhip_tim_max', 0)}
        
        SpO2 (%):
          • Trung bình: {thong_ke.get('spo2_tb', 0)}
          • Min: {thong_ke.get('spo2_min', 0)} | Max: {thong_ke.get('spo2_max', 0)}
        
        CO2 (ppm):
          • Trung bình: {thong_ke.get('co2_tb', 0)}
          • Min: {thong_ke.get('co2_min', 0)} | Max: {thong_ke.get('co2_max', 0)}
        """
        self.label_thong_ke.setText(text)

    def ve_bieu_do(self, df):
        self.bieu_do.ve(df)

    def xem_lich_su(self, df):
        dialog = QDialog(self)
        dialog.setWindowTitle("Lịch sử đo sức khỏe")
        dialog.resize(900, 500)

        layout = QVBoxLayout(dialog)

        if df.empty:
            empty_label = QLabel("Không có dữ liệu lịch sử.")
            empty_label.setWordWrap(True)
            layout.addWidget(empty_label)
            dialog.setLayout(layout)
            dialog.exec()
            return

        table = QTableWidget()
        table.setColumnCount(len(df.columns))
        table.setHorizontalHeaderLabels([
            "Thời gian", "Cân nặng", "Chiều cao", "BMI", "Nhịp tim", "SpO2", "CO2"
        ])
        table.setRowCount(len(df))
        table.setAlternatingRowColors(True)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        for row_index, row in df.iterrows():
            for col_index, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
                table.setItem(row_index, col_index, item)

        layout.addWidget(table)
        dialog.setLayout(layout)
        dialog.exec()
    
    def lam_moi(self):
        """Clear all input fields and reset display"""
        self.input_can_nang.clear()
        self.input_chieu_cao.clear()
        self.input_nhip_tim.clear()
        self.input_spo2.clear()
        self.input_co2.clear()
        self.label.setText("")
        self.input_can_nang.setFocus()