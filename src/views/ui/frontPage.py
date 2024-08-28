from PySide6.QtWidgets import QMainWindow, QMenu, QLabel, QFrame, QTableWidgetItem
from PySide6.QtGui import QAction, QFont
from PySide6.QtCore import Qt
import utils

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

    def update_diagnostic_message(self, message: dict):
        """
        Update the diagnostic message in the GUI.
        Show the diagnostic message in the diagnostic tab (table widget) called diagnostic_table.
        The message is a dictionary with the following keys: 'Fault_Class', 'Diag_Code', 'Timestamp' (send with the message),  'Sel_Cells_NTC': 1, 'Cell_Num', 'timestamp' (time of the can message).
        Diag_Code is a multiplexor. 0x0: Not_Cell_NTC, 0x1: Cell_Num, 0x2: NTC_Num
        :param message: The diagnostic message
        """
        print(message)
        # Temporarily disable sorting
        self.diagnostic_table.setSortingEnabled(False)

        # Add the message to the table. The timestamp is a new row and the rest of the data is an item
        # the row is the timestamp in dd/mm/yyyy hh:mm:ss format
        row = self.diagnostic_table.rowCount()
        self.diagnostic_table.insertRow(row)

        self.diagnostic_table.setItem(
            row, 0, QTableWidgetItem(utils.date_from_timestamp(message["timestamp"]))
        )
        self.diagnostic_table.setItem(
            row, 1, QTableWidgetItem(str(message["Diag_Code"]))
        )

        self.diagnostic_table.setItem(
            row, 2, QTableWidgetItem(str(message["Fault_Class"]))
        )

        if message["Sel_Cells_NTC"] == 0x1:
            self.diagnostic_table.setItem(
                row, 3, QTableWidgetItem(str(message["Cell_Num"]))
            )
        elif message["Sel_Cells_NTC"] == 0x2:
            self.diagnostic_table.setItem(
                row, 3, QTableWidgetItem(str(message["NTC_Num"]))
            )
        elif message["Sel_Cells_NTC"] == 0x0:
            self.diagnostic_table.setItem(row, 3, QTableWidgetItem("NA"))

        # Re-enable sorting
        self.diagnostic_table.setSortingEnabled(True)

        # Optionally, sort the table by the timestamp column (assuming it's column 0)
        self.diagnostic_table.sortItems(0, Qt.DescendingOrder)

        # Resize the columns to fit the content
        self.diagnostic_table.resizeColumnsToContents()
