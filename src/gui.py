import sys

from PySide6.QtWidgets import QApplication

sys.path.append("interface")
from interface.frontPage import MySideBar


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MySideBar()
    window.show()
    app.exec_()
