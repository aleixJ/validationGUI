import sys
from PySide6.QtWidgets import QApplication

from .ui.frontPage import MyMainWindow

import utils


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

    def update_data(self, data: dict) -> None:
        """
        Update the data in the GUI
        :param data: The data to update (decoded CAN message)
        """
        for key, value in data.items():
            base_name = utils.base_name(key)
            if base_name.lower() == "cell_voltage":
                # get the index of the cell (last part of the key)
                index = int(key.split("_")[-1])
                self.main_window.update_cell_voltatge(index, str(value))
            if base_name.lower() == "cell_soc":
                # get the index of the cell (last part of the key)
                index = int(key.split("_")[-1])
                self.main_window.update_cell_soc(index, str(value))
