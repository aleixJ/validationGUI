from PySide6.QtWidgets import QMainWindow, QMenu
from PySide6.QtGui import QAction

from .ui_index import Ui_MainWindow

"""
This file is the intermediary between the ui_interface.py and the gui_view.py files.
"""


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # type: ignore
        self.setWindowTitle("SlideBarMenu")

        # Connect buttons to switch pages

        self.dashboard_btn.clicked.connect(self.switch_to_dashboard)
        self.diagnostic_btn.clicked.connect(self.switch_to_diagnostic)
        self.settings_btn.clicked.connect(self.switch_to_settings)
        self.update_cell_temperature(1, "20")

    def switch_to_dashboard(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_diagnostic(self):
        self.stackedWidget.setCurrentIndex(1)

    def switch_to_settings(self):
        self.stackedWidget.setCurrentIndex(2)

    def update_cell_temperature(self, index: int, temperature: str):
        """
        Update the cell temperature in the GUI
        :param index: The index of the cell
        :param temperature: The temperature of the cell
        """
        variable = getattr(self, f"cell{index}_temperature")
        # check if the variable exists in the ui file
        variable.setText(temperature)
