from PySide6.QtCore import Signal
from PySide6.QtWidgets import QMainWindow

from .ui_settings import Ui_Dialog

from typing import Union
from typing import Any


class MySettingsWindow(QMainWindow, Ui_Dialog):
    settings_accepted = Signal(dict)

    def __init__(self):
        super().__init__()
        self.setupUi(self)  # type: ignore
        self.setWindowTitle("Settings")

        # list of interfaces
        self.interfaces = []
        # Connect buttons to switch pages
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

    def set_interfaces(self, interfaces: list[dict[str, Union[str, int]]]) -> None:
        """
        Set the available interfaces in the comboBox. (interface - channel)
        :param interfaces: The available interfaces
        """
        self.interfaces = []
        for interface in interfaces:
            # Save the interface in a list
            self.interfaces.append(interface)
            # Add the interface to the comboBox
            self.comboBox.addItem(f"{interface['interface']} - {interface['channel']}")

    def accept(self) -> None:
        # check if 'comboBox' is selected
        if not self.comboBox.currentText().lower() == "select an interface and channel":
            # Emit the signal with the selected channel. '-1' because the placeholder
            self.settings_accepted.emit(
                self.interfaces[self.comboBox.currentIndex() - 1]
            )
            # close the window
            self.close()

    def reject(self) -> None:
        self.close()
