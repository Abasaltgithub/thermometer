import serial
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the serial port and baud rate (make sure they match your Arduino settings)
# Replace '/dev/tty.usbserial-210' with your Arduino's serial port
ser = serial.Serial('/dev/tty.usbserial-2110', 9600)

# Initialize lists to store data
temperature_data = []
humidity_data = []

# Create subplots for temperature and humidity with added vertical space
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
fig.subplots_adjust(hspace=0.5)  # Adjust the vertical space


def update_plot(frame):
    try:
        # Read data from the Arduino
        data = ser.readline().decode('utf-8').strip()

        # Split data into temperature and humidity parts
        temp_start = data.find("Temp: ") + len("Temp: ")
        temp_end = data.find(" C", temp_start)
        rel_hum_start = data.find("Humidity: ") + len("Humidity: ")
        rel_hum_end = data.find(" %", rel_hum_start)

        temperature_str = data[temp_start:temp_end]
        humidity_str = data[rel_hum_start:rel_hum_end]

        try:
            temperature = float(temperature_str)
            humidity = float(humidity_str)

            temperature_data.append(temperature)
            humidity_data.append(humidity)

            # Update the plot
            ax1.clear()
            ax1.plot(temperature_data, label='Temperature (C)')
            ax1.set_title('Real-Time Temperature Data')
            ax1.set_ylabel('Temperature (C)')
            ax1.legend()

            ax2.clear()
            ax2.plot(humidity_data, label='Humidity (%)', color='orange')
            ax2.set_title('Real-Time Humidity Data')
            ax2.set_xlabel('Time')
            ax2.set_ylabel('Humidity (%)')
            ax2.legend()
        except ValueError:
            pass  # Skip lines that can't be converted to float
    except KeyboardInterrupt:
        print("Serial communication stopped.")
        ser.close()


# Create an animation that updates the plot
ani = FuncAnimation(fig, update_plot, interval=1000)

# Display the plot
plt.show()
