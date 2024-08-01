import sys
from PySide6.QtWidgets import QApplication

from .ui.frontPage import MyMainWindow
from .ui.settingsPage import MySettingsWindow

import utils

from typing import Union
from typing import Any


class gui_view:
    """
    View class for the GUI
    """

    # Constructor
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.settings_window = MySettingsWindow()
        self.main_window = MyMainWindow()
        self.interface_selected = None

        # Connect the settings accepted signal to a slot
        self.settings_window.settings_accepted.connect(self.on_settings_accepted)

    def show_settings(self, interfaces: list[dict[str, Union[str, int]]]) -> None:
        """
        Show the settings window.
        :param interfaces: The available interfaces (interfaces and channels)
        """
        self.settings_window.set_interfaces(interfaces)
        self.settings_window.show()

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

    def on_settings_accepted(self, interface: dict[str, Union[str, int]]) -> None:
        """
        Slot to handle the accepted settings
        :param interface: The selected interface
        """
        self.interface_selected = interface

    def get_interface_selected(self) -> Union[dict[str, Union[str, int]], None]:
        """
        Get the selected interface
        :return: The selected interface
        """
        return self.interface_selected
