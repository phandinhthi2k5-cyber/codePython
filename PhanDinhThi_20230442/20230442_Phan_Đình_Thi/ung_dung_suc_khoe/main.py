import sys
from PyQt6.QtWidgets import QApplication
from view.cua_so_chinh import CuaSoChinh
from controller.xu_ly_suc_khoe import XuLySucKhoe

if __name__ == "__main__":
    app = QApplication(sys.argv)

    view = CuaSoChinh()
    controller = XuLySucKhoe(view)

    view.showMaximized()
    sys.exit(app.exec())