from PySide6.QtWidgets import QMainWindow, QMenu
from PySide6.QtGui import QAction
from interface.ui_interface import Ui_MainWindow

"""
This class is the intermediary between the ui_interface.py and the gui.py files.
"""


class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("SlideBarMenu")

        # Connect buttons to switch pages

        self.dashboard_btn.clicked.connect(self.switch_to_dashboard)
        self.diagnostic_btn.clicked.connect(self.switch_to_diagnostic)
        self.settings_btn.clicked.connect(self.switch_to_settings)

    def switch_to_dashboard(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_diagnostic(self):
        self.stackedWidget.setCurrentIndex(1)

    def switch_to_settings(self):
        self.stackedWidget.setCurrentIndex(2)
