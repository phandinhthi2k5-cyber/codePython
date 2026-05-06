from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

class BieuDo(FigureCanvas):
    def __init__(self):
        self.figure = Figure(figsize=(8, 6))
        super().__init__(self.figure)
        self.setMinimumHeight(400)
        self.setMinimumWidth(500)

    def ve(self, df):
        self.figure.clear()
        
        if df.empty:
            ax = self.figure.add_subplot(111)
            ax.text(0.5, 0.5, 'Không có dữ liệu', ha='center', va='center', fontsize=14)
            ax.set_xlim(0, 1)
            ax.set_ylim(0, 1)
            ax.axis('off')
            self.draw()
            return
        
        # Tạo 4 subplot cho 4 chỉ số
        fig = self.figure
        
        # BMI
        ax1 = fig.add_subplot(2, 2, 1)
        ax1.plot(range(len(df)), df["bmi"], marker='o', linestyle='-', linewidth=2, markersize=6, color='#FF6B6B', label='BMI')
        ax1.axhline(y=18.5, color='orange', linestyle='--', alpha=0.5, label='Thiếu cân')
        ax1.axhline(y=25, color='orange', linestyle='--', alpha=0.5, label='Thừa cân')
        ax1.axhline(y=30, color='red', linestyle='--', alpha=0.5, label='Béo phì')
        ax1.set_ylabel('BMI')
        ax1.set_title('Chỉ số BMI')
        ax1.grid(True, alpha=0.3)
        ax1.legend(fontsize=8)

        # Nhịp tim
        ax2 = fig.add_subplot(2, 2, 2)
        ax2.plot(range(len(df)), df["nhip_tim"], marker='s', linestyle='-', linewidth=2, markersize=6, color='#4ECDC4', label='Nhịp tim')
        ax2.axhline(y=60, color='orange', linestyle='--', alpha=0.5, label='Nhịp tim thấp')
        ax2.axhline(y=100, color='orange', linestyle='--', alpha=0.5, label='Nhịp tim cao')
        ax2.axhline(y=120, color='red', linestyle='--', alpha=0.5, label='Nhịp tim nguy hiểm')
        ax2.set_ylabel('Nhịp tim (bpm)')
        ax2.set_title('Nhịp Tim')
        ax2.grid(True, alpha=0.3)
        ax2.legend(fontsize=8)

        # SpO2
        ax3 = fig.add_subplot(2, 2, 3)
        ax3.plot(range(len(df)), df["spo2"], marker='^', linestyle='-', linewidth=2, markersize=6, color='#95E1D3', label='SpO2')
        ax3.axhline(y=90, color='red', linestyle='--', alpha=0.5, label='SpO2 nguy hiểm')
        ax3.axhline(y=95, color='orange', linestyle='--', alpha=0.5, label='SpO2 thấp')
        ax3.set_ylabel('SpO2 (%)')
        ax3.set_title('Độ bão hòa oxy trong máu')
        ax3.set_ylim(80, 102)
        ax3.grid(True, alpha=0.3)
        ax3.legend(fontsize=8)

        # CO2
        ax4 = fig.add_subplot(2, 2, 4)
        ax4.plot(range(len(df)), df["co2"], marker='D', linestyle='-', linewidth=2, markersize=6, color='#F38181', label='CO2')
        ax4.axhline(y=20, color='orange', linestyle='--', alpha=0.5, label='CO2 thấp')
        ax4.axhline(y=40, color='orange', linestyle='--', alpha=0.5, label='CO2 cao')
        ax4.axhline(y=50, color='red', linestyle='--', alpha=0.5, label='CO2 nguy hiểm')
        ax4.set_ylabel('CO2 (ppm)')
        ax4.set_title('Nồng độ CO2')
        ax4.grid(True, alpha=0.3)
        ax4.legend(fontsize=8)

        plt.tight_layout()
        self.draw()