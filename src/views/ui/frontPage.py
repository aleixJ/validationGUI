from PySide6.QtWidgets import QMainWindow, QMenu
from PySide6.QtGui import QAction

from .ui_index import Ui_MainWindow

"""
This file is the intermediary between the ui_interface.py and the gui.py files.
"""


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("SlideBarMenu")

        # Connect buttons to switch pages

        self.dashboard_btn.clicked.connect(self.switch_to_dashboard)
        self.diagnostic_btn.clicked.connect(self.switch_to_diagnostic)
        self.settings_btn.clicked.connect(self.switch_to_settings)
        print("UI file loaded")
        self.update_cell_temperature(1, "20")

    def switch_to_dashboard(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_diagnostic(self):
        self.stackedWidget.setCurrentIndex(1)

    def switch_to_settings(self):
        self.stackedWidget.setCurrentIndex(2)

    def update_cell_temperature(self, index, temperature):
        "Modifies the temperature of the cell at the given index"
        variable = getattr(self, f"cell{index}_temperature")
        # check if the variable exists in the ui file
        variable.setText(temperature)
