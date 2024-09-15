import argparse
import random
import threading
import time

import can
import cantools

import os


def create_and_send_message(bus, message, signal_values):
    # Encode the signal values into a sequence of bytes
    data = message.encode(signal_values)

    # Create a CAN message
    can_message = can.Message(
        arbitration_id=message.frame_id, data=data, is_extended_id=False
    )

    # Send the CAN message
    bus.send(can_message)


def send_can_messages(bus, db, delay, stop_event):
    while not stop_event.is_set():
        for message in db.messages:
            if message.name in [
                "Cell_Voltages_01",
                "Cell_Voltages_02",
                "Cell_Voltages_03",
                "Cell_Voltages_04",
                "Cell_Voltages_05",
            ]:
                # Create a dictionary of signal values
                signal_values = {
                    signal.name: random.randint(3200, 4100)
                    for signal in message.signals
                }

                # Encode and send the message
                create_and_send_message(bus, message, signal_values)

            if message.name == "Cell_Temperatures":
                # Create a dictionary of signal values
                signal_values = {
                    signal.name: random.randint(25, 45) for signal in message.signals
                }

                # Encode and send the message
                create_and_send_message(bus, message, signal_values)

            if message.name == "BMS_State":
                # Create a dictionary of signal values
                signal_values = {
                    "BMS_State_Machine": "Idle state",
                    "Peripheral_status": 0,
                    "FC_Level": "FC_None",
                    "InternalErrorMask": 0,
                }

            if message.name == "Diagnostic_Message":
                # Create a dictionary of signal values
                signal_values = {
                    "Fault_Class": random.randint(0,3),
                    "Diag_Code": random.randint(0, 98),
                    "Sel_Cells_NTC": 1,
                    "Cell_Num": 1,
                    "Timestamp": time.time(),
                }

                # Encode and send the message
                create_and_send_message(bus, message, signal_values)

        # Wait for a bit before sending the next message
        time.sleep(delay)


def simulate_bms(interface, channel, bitrate, dbc_file_path, delay):
    # Parse the DBC file
    db = cantools.database.load_file(dbc_file_path)

    # Create a new CAN bus
    bus = can.interface.Bus(channel=channel, interface=interface, bitrate=bitrate)

    # Create a stop event
    stop_event = threading.Event()

    # Start a new thread that sends CAN messages periodically
    thread = threading.Thread(
        target=send_can_messages, args=(bus, db, delay, stop_event)
    )
    thread.start()

    return stop_event, thread


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simulate BMS")
    parser.add_argument(
        "--interface", type=str, default="kvaser", help="Interface name"
    )
    parser.add_argument("--channel", type=int, default=0, help="Channel number")
    parser.add_argument("--bitrate", type=int, default=500000, help="Bitrate in bps")
    parser.add_argument(
        "--dbc",
        type=str,
        default="..\\DBC\\BMS_multiplex.dbc",
        help="DBC file path",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=1,
        help="Delay between groups of messages in seconds",
    )
    args = parser.parse_args()

    stop_event, thread = simulate_bms(
        args.interface, args.channel, args.bitrate, args.dbc, args.delay
    )

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        stop_event.set()
        thread.join()
