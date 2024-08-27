from PySide6.QtWidgets import QMainWindow, QMenu, QLabel, QFrame
from PySide6.QtGui import QAction, QFont

from .ui_index import Ui_MainWindow

"""
This file is the intermediary between the ui_interface.py and the gui_view.py files.
"""


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # type: ignore
        self.setWindowTitle("Validation BMS")

        # Connect buttons to switch pages

        self.dashboard_btn.clicked.connect(self.switch_to_dashboard)
        self.diagnostic_btn.clicked.connect(self.switch_to_diagnostic)
        self.settings_btn.clicked.connect(self.switch_to_settings)

    def resize_dashboard(self):
        """
        Resize the dashboard
        """
        # Calculate the font size based on the size of the window
        font_size = int((12 / 600) * (min(self.width(), self.height())))
        # Loop through all the labels in the dashboard
        for label in self.dashboard.findChildren(QLabel):
            # check if the label is a title
            if "title" in label.objectName():
                # increase the font size of the title and bold it
                label.setFont(QFont("Arial", font_size + 2, QFont.Bold))
            else:
                label.setFont(QFont("Arial", font_size))

    def resizeEvent(self, event):
        self.resize_dashboard()
        super().resizeEvent(event)

    def switch_to_dashboard(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_diagnostic(self):
        self.stackedWidget.setCurrentIndex(1)

    def switch_to_settings(self):
        self.stackedWidget.setCurrentIndex(2)

    def update_cell_voltatge(self, index: int, voltatge: str):
        """
        Update the cell voltage in the GUI
        :param index: The index of the cell
        :param voltatge: The voltage of the cell
        """
        variable = getattr(self, f"cell{index}_voltage")
        variable.setText(voltatge + " mV")

    def update_cell_soc(self, index: int, soc: str):
        """
        Update the cell state of charge in the GUI
        :param index: The index of the cell
        :param soc: The state of charge of the cell
        """
        variable = getattr(self, f"cell{index}_soc")
        variable.setText(soc + " %")
