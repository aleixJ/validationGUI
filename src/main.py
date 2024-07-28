import sys
import threading

from models.can_model import can_model
from views.gui_view import gui_view


def receive_messages(controller: can_model) -> None:
    while True:
        controller.receive_can_message()


def main():
    try:
        # Create a new can_model object
        can_m = can_model()
        # Create a new gui_view object
        gui_v = gui_view()

        # Add the gui_view object as a listener to the can_model object
        can_m.add_listener(gui_v.update_data)

        # Start the thread to receive CAN messages
        receive_thread = threading.Thread(target=receive_messages, args=(can_m,))
        receive_thread.daemon = True
        receive_thread.start()

        # Start the GUI
        gui_v.show()
    except KeyboardInterrupt:
        if can_m is not None:
            del can_m


if __name__ == "__main__":
    main()
