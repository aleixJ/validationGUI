import can_controller
import plot
import threading


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
        # Start the plotting
        plot.plotBMS(controller).show()

    except KeyboardInterrupt:
        del controller


if __name__ == "__main__":
    main()
