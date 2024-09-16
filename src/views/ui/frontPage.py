from PySide6.QtWidgets import QMainWindow, QMenu, QLabel, QFrame, QTableWidgetItem, QFileDialog
from PySide6.QtGui import QAction, QFont, QColor
from PySide6.QtCore import Qt
import utils
import time
import csv

from .ui_index import Ui_MainWindow

"""
This file is the intermediary between the ui_interface.py and the gui_view.py files.
"""

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, config):
        super().__init__()
        self.config = config  # Store the config object
        self.setupUi(self)  # type: ignore
        self.setWindowTitle("Validation BMS")

        # Connect buttons to switch pages
        self.dashboard_btn.clicked.connect(self.switch_to_dashboard)
        self.diagnostic_btn.clicked.connect(self.switch_to_diagnostic)
        self.settings_btn.clicked.connect(self.switch_to_settings)
        
        # Connect the diagnostic page.
        self.pause_diagnostic_btn.clicked.connect(self.change_color_pause_diagnostic)
        self.clear_diagnostic_btn.clicked.connect(self.clear_diagnostic_table)
        self.save_diagnostic_btn.clicked.connect(self.save_diagnostic_table)

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
        
    def change_color_pause_diagnostic(self):
        if self.pause_diagnostic_btn.isChecked():
            self.pause_diagnostic_btn.setStyleSheet("color: red")
        else:
            self.pause_diagnostic_btn.setStyleSheet("color: green")
            
    def clear_diagnostic_table(self):
        self.diagnostic_table.setRowCount(0)
        
    def save_diagnostic_table(self):
        # Get the current time and format it as YYYY-MM-DD--HH-MM-SS
        default_name = time.strftime("%Y-%m-%d--%H-%M-%S")
        
        # Open a file dialog to select the file path and name
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Diagnostic Table", f"{default_name}.csv", "CSV Files (*.csv)")
        
        if file_path:
            # Open the file in write mode
            with open(file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                
                # Write the header
                headers = [self.diagnostic_table.horizontalHeaderItem(i).text() for i in range(self.diagnostic_table.columnCount())]
                writer.writerow(headers)
                
                # Write the table data
                for row in range(self.diagnostic_table.rowCount()):
                    row_data = [self.diagnostic_table.item(row, column).text() if self.diagnostic_table.item(row, column) else '' for column in range(self.diagnostic_table.columnCount())]
                    writer.writerow(row_data)

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
        # check if the table is paused
        if self.pause_diagnostic_btn.isChecked():
            return
        
        # Check the Fault_Class and set the color
        fault_class = str(message["Fault_Class"])
        color = self.config.diagnostic_colors.get(fault_class, self.config.diagnostic_colors['default'])
        
        # Temporarily disable sorting
        self.diagnostic_table.setSortingEnabled(False)
        
        # if the table have more than max_diagnostic_messages rows, remove the last one
        if self.diagnostic_table.rowCount() > self.config.max_diagnostic_messages:
            self.diagnostic_table.removeRow(self.diagnostic_table.rowCount() - 1)

        # Add the message to the table. The timestamp is a new row and the rest of the data is an item
        # the row is the timestamp in dd/mm/yyyy hh:mm:ss format
        row = self.diagnostic_table.rowCount()
        self.diagnostic_table.insertRow(row)

        timestamp_item = QTableWidgetItem(utils.date_from_timestamp(time.time(), self.config.date_format))
        diag_code_item = QTableWidgetItem(str(message["Diag_Code"]))
        fault_class_item = QTableWidgetItem(fault_class)

        # Set the color for the items
        timestamp_item.setForeground(QColor(color))
        diag_code_item.setForeground(QColor(color))
        fault_class_item.setForeground(QColor(color))

        self.diagnostic_table.setItem(row, 0, timestamp_item)
        self.diagnostic_table.setItem(row, 1, diag_code_item)
        self.diagnostic_table.setItem(row, 2, fault_class_item)

        if message["Sel_Cells_NTC"] == 0x1:
            cell_num_item = QTableWidgetItem(str(message["Cell_Num"]))
        elif message["Sel_Cells_NTC"] == 0x2:
            cell_num_item = QTableWidgetItem(str(message["NTC_Num"]))
        elif message["Sel_Cells_NTC"] == 0x0:
            cell_num_item = QTableWidgetItem("NA")
        else:
            cell_num_item = QTableWidgetItem("")

        # Set the color for the cell/NTC number item
        cell_num_item.setForeground(QColor(color))
        self.diagnostic_table.setItem(row, 3, cell_num_item)
        
        # Re-enable sorting
        self.diagnostic_table.setSortingEnabled(True)

        # Optionally, sort the table by the timestamp column (assuming it's column 0)
        self.diagnostic_table.sortItems(0, Qt.DescendingOrder)

        # Resize the columns to fit the content
        self.diagnostic_table.resizeColumnsToContents()
        # Add a little extra width to the columns
        for column in range(self.diagnostic_table.columnCount()):
            self.diagnostic_table.setColumnWidth(column, self.diagnostic_table.columnWidth(column) + 20)