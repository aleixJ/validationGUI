import sys
import models.can_controller as can_controller
import plot
import threading

import views.gui as gui
from pathlib import Path


def receive_messages(controller):
    while True:
        controller.receive_can_message()


def main():
    try:
        # Create a new can_controller object
        controller = can_controller.can_controller()

        # Start the thread to receive CAN messages
        receive_thread = threading.Thread(target=receive_messages, args=(controller,))
        receive_thread.daemon = True
        receive_thread.start()

        # Start the GUI
        gui.start_gui()
    except KeyboardInterrupt:
        del controller


if __name__ == "__main__":
    main()
