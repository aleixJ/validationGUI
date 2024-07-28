import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.dates as mdates
from datetime import datetime
import matplotlib.lines


############################################
# NOT USED
############################################


class plotBMS:
    """
    Class to plot data from the BMS
    The plot will show the cell voltages and cell temperatures
    The plot will be updated in real-time using the animation module
    """

    def __init__(self, can_model):
        self.can_model = can_model
        self.fig, (self.ax1, self.ax2) = plt.subplots(2, 1)

        # Initialize empty lines for temperature and voltage plots
        self.lines_temp = [
            self.ax1.plot([], [], label=f"Temperature {i+1}")[0] for i in range(6)
        ]
        self.lines_volt = [
            self.ax2.plot([], [], label=f"Voltage {i+1}")[0] for i in range(18)
        ]

        self.ani_temp = animation.FuncAnimation(
            self.fig, self.update_temperature, interval=1000, cache_frame_data=False
        )
        self.ani_volt = animation.FuncAnimation(
            self.fig, self.update_voltage, interval=1000, cache_frame_data=False
        )

        self._setup_axes()

    def _setup_axes(self) -> None:
        """
        Setup the axes for the plot. Set the title, labels, and legend
        """
        self.ax1.set_title("Cell Temperatures")
        self.ax1.set_xlabel("Timestamp")
        self.ax1.set_ylabel("Temperature (°C)")
        self.ax1.legend(loc="upper right")
        self.ax1.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M:%S"))

        self.ax2.set_title("Cell Voltages")
        self.ax2.set_xlabel("Timestamp")
        self.ax2.set_ylabel("Voltage (mV)")
        self.ax2.legend(loc="upper right")
        self.ax2.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M:%S"))

    def update_temperature(self, i: int) -> list[matplotlib.lines.Line2D]:
        """
        Update the temperature plot with new data
        :param i: The frame number
        :return: The updated lines
        """
        for idx, (temp_name, temp_dict) in enumerate(
            self.can_model.data["Cell_Temperatures"].items()
        ):
            if temp_dict is not None:
                self.lines_temp[idx].set_data(
                    mdates.date2num(list(temp_dict["timestamp"])),
                    list(temp_dict["value"]),
                )
        self.ax1.relim()
        self.ax1.autoscale_view()
        return self.lines_temp

    def update_voltage(self, i: int) -> list[matplotlib.lines.Line2D]:
        """
        Update the voltage plot with new data
        :param i: The frame number
        :return: The updated lines
        """
        for idx, (volt_name, volt_dict) in enumerate(
            self.can_model.data["Cell_Voltages"].items()
        ):
            if volt_dict is not None:
                self.lines_volt[idx].set_data(
                    mdates.date2num(list(volt_dict["timestamp"])),
                    list(volt_dict["value"]),
                )
        self.ax2.relim()
        self.ax2.autoscale_view()
        return self.lines_volt

    def show(self) -> None:
        """
        Show the plot
        """
        plt.tight_layout()
        plt.show()
