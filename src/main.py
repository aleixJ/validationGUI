import sys
import threading

from models.can_model import can_model
from views.gui_view import gui_view

from config import Config  # Import the Config class

running = True

def receive_messages(controller: can_model) -> None:
    while running:
        controller.receive_can_message()

def main():
    global running
    try:
        # Create a new Config object
        config = Config()
        config.load_settings('settings.yaml')
        
        # Create a new can_model object
        can_m = can_model()

        # Create a new gui_view object
        gui_v = gui_view(config)  # Pass the config object to gui_view
        gui_v.show_settings(can_m.list_available_interfaces())

        # Wait for the settings to be accepted
        while gui_v.get_interface_selected() is None:
            gui_v.app.processEvents()

        # Set the interface and channel
        can_m.set_interface(gui_v.get_interface_selected()["interface"])
        can_m.set_channel(gui_v.get_interface_selected()["channel"])

        # Create a new CAN bus
        can_m.create_can_bus()
                  
        # Add the gui_view object as a listener to the can_model object
        can_m.add_listener(lambda data: gui_v.signals.update_data_signal.emit(data))

        # Start the thread to receive CAN messages
        receive_thread = threading.Thread(target=receive_messages, args=(can_m,))
        receive_thread.daemon = True
        receive_thread.start()

        # Start the GUI
        gui_v.show()
    except KeyboardInterrupt:
        running = False
        if can_m is not None:
            del can_m

if __name__ == "__main__":
    main()