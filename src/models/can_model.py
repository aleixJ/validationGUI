import can
import cantools
import re
import sys

# include the path for the utils.py file (if this file is executed directly)
sys.path.append("src")
import utils

from typing import Union
from typing import Any
from collections import deque


class can_model:
    """
    Controller class for the CAN communication.
    Model because it is responsible for the data and the communication with the CAN bus.
    """

    # Constructor
    def __init__(
        self,
        channel: Union[str, int] = 1,
        interface: str = "kvaser",
        bitrate: int = 500000,
    ):
        """
        Constructor for the can_model class
        :param channel: The channel number to use for CAN communication
        :param interface: The interface to use for CAN communication
        :param bitrate: The bitrate to use for CAN communication
        """
        self.channel = channel
        self.interface = interface
        self.bitrate = bitrate
        self.bus = None  # Wait the settings to create the bus
        self.db = self.load_dbc_file(path="DBC/BMS_multiplex.dbc")
        self.data = self.setup_data()  # Not used in version
        self.listeners = []
        # utils.print_data_structure(self.data)  # print the dictionary

    # Destructor
    def __del__(self):
        if self.bus is not None:
            self.bus.shutdown()

    def list_available_interfaces(self) -> list[dict[str, Union[str, int]]]:
        """
        List all available CAN interfaces
        :return: A list of available CAN interfaces
        """
        configs = can.detect_available_configs(self.interface)
        return [
            {"interface": config["interface"], "channel": config["channel"]}
            for config in configs
        ]

    def print_available_interfaces(self) -> None:
        """
        Print all available CAN interfaces
        """
        configs = self.list_available_interfaces()
        for config in configs:
            print(f"Interface: {config['interface']}, Channel: {config['channel']}")

    def set_interface(self, interface: str) -> None:
        """
        Set the interface to use for CAN communication
        :param interface: The interface to use
        """
        if interface in [
            config["interface"] for config in self.list_available_interfaces()
        ]:
            self.interface = interface

    def set_channel(self, channel: Union[str, int]) -> None:
        """
        Set the channel to use for CAN communication
        :param channel: The channel to use
        """
        if channel in [
            config["channel"] for config in self.list_available_interfaces()
        ]:
            self.channel = channel

    def create_can_bus(self) -> None:
        """
        Create a new CAN bus
        """
        self.bus = can.interface.Bus(
            channel=self.channel, interface=self.interface, bitrate=self.bitrate
        )

    def load_dbc_file(self, path: str) -> Any:
        """
        Load a DBC file
        :param dbc_file_path: The path to the DBC file
        """
        return cantools.db.load_file(path)

    def get_interface_and_channel(self) -> dict[str, Union[str, int]]:
        """
        Get the interface and channel
        :return: The interface and channel
        """
        return {"interface": self.interface, "channel": self.channel}

    def setup_data(
        self,
    ) -> dict[str, dict[str, Union[None, dict[str, deque[Any]]]]]:
        """
        Setup the data structure that will be used to store the received data
        :return: The data structure
        """
        grouped_messages = {}

        for message in self.db.messages:
            # Use regex to remove trailing numbers and underscores
            base_name = utils.base_name(message.name)
            if base_name not in grouped_messages:
                grouped_messages[base_name] = {}
            for signal in message.signals:
                grouped_messages[base_name][signal.name] = None
        # sort only the signals keys in the dictionary. Prevent _1, _10.
        for base_name in grouped_messages:
            grouped_messages[base_name] = dict(
                sorted(grouped_messages[base_name].items(), key=utils.natural_sort_key)
            )

        return grouped_messages

    def decode_message(self, message: can.Message) -> tuple[dict[str, Any], str]:
        """
        Decode a CAN message
        :param message: The CAN message to decode
        :return: The decoded message and the message name
        """
        # decoded have this structe: {'Cell_Voltage_5': 3735, 'Cell_Voltage_6': 4036, 'Cell_Voltage_7': 4024, 'Cell_Voltage_8': 3274, 'timestamp': 1721699728.707768}
        decoded_message = self.db.decode_message(message.arbitration_id, message.data)
        message_name = self.db.get_message_by_frame_id(message.arbitration_id).name
        return decoded_message, message_name

    def save_data(self, message: dict[str, Any]) -> None:
        """
        Save the data already decoded in memory. The data will be saved in self.data.
        :param message: The message to save
        """
        for rcv_key, rcv_value in message.items():
            for key, value in self.data.items():
                if rcv_key in value:
                    # check if the data is a list
                    if value[rcv_key] is None:
                        value[rcv_key] = {
                            "timestamp": deque(maxlen=100),
                            "value": deque(maxlen=100),
                        }
                    # append the data to the list
                    value[rcv_key]["timestamp"].append(message["timestamp"])  # type: ignore
                    value[rcv_key]["value"].append(rcv_value)  # type: ignore

    def receive_can_message(self) -> Union[dict[str, Any], None]:
        """
        Receive a CAN message. When a message is received, decode it, save the data in memory and return it.
        :return: The received CAN message decoded into a dictionary of signal values
        """
        if self.bus is not None:
            message: can.Message | None = self.bus.recv()
        else:
            message = None
        if message is not None:
            decoded, message_name = self.decode_message(message)
            decoded["timestamp"] = message.timestamp
            # save the data in self.data
            self.save_data(decoded)
            # notify the listeners. Return the decoded message and the message name as a dictionary. Decoded message is a dictionary of signal values.
            self._notify_listeners(
                {"decoded_message": decoded, "message_name": message_name}
            )
            return decoded
        else:
            return None

    def parse_database(self) -> None:
        """
        Parse the database
        """
        for message in self.db.messages:
            print(f"Message: {message.name}")
            for signal in message.signals:
                print(f"Signal: {signal.name}")

    def add_listener(self, listener: Any) -> None:
        """
        Add a listener to the list of listeners
        :param listener: The listener to add
        """
        self.listeners.append(listener)

    def _notify_listeners(self, data: dict[str, Any]) -> None:
        """
        Notify all listeners.
        :param data: The data to send to the listeners
        """
        for listener in self.listeners:
            listener(data)


if __name__ == "__main__":
    temp = can_model()
    while True:
        message = temp.receive_can_message()
        if message is not None:
            print(message)
