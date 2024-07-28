import sys
from PySide6.QtWidgets import QApplication

from .ui.frontPage import MyMainWindow


class gui_view:
    """
    View class for the GUI
    """

    # Constructor
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.main_window = MyMainWindow()

    def show(self) -> None:
        """
        Show the GUI
        """
        self.main_window.show()
        self.app.exec_()

    def update_data(self, data: dict[str, dict[str, str]]) -> None:
        """
        Update the data in the GUI
        :param data: The data to update
        """
        for key, value in data.items():
            if key == "cell_temperature":
                for cell, temperature in value.items():
                    self.main_window.update_cell_temperature(int(cell), temperature)
            # Add more elif statements for other data types
