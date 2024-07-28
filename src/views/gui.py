import sys
from PySide6.QtWidgets import QApplication

from .ui.frontPage import MyMainWindow


def start_gui():
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    app.exec_()
