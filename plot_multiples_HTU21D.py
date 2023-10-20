import serial
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time
import csv

# Define the list of serial ports
serial_ports = ['/dev/tty.usbserial-21340', '/dev/tty.usbserial-21410',
                '/dev/tty.usbserial-21420', '/dev/tty.usbserial-21430', '/dev/tty.usbserial-21440']

# Create a list of Serial objects
ser_ports = [serial.Serial(port, 9600) for port in serial_ports]

# Create CSV file objects to write temperature and humidity data
csv_file = open('S5_test.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)

# Define column headers for temperature and humidity data for each sensor
columns = []
for i in range(len(serial_ports)):
    columns.extend([f'S{i + 1} Temp (C)', f'S{i + 1} Humidity (%)'])
csv_writer.writerow(columns)

# Initialize lists to store data for each port
temperature_data = [([]) for _ in serial_ports]
humidity_data = [([]) for _ in serial_ports]

# Create subplots for temperature and humidity with added vertical space
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
fig.subplots_adjust(hspace=0.5)  # Adjust the vertical space

# Change this to the number of sensors you have
sensor_count = len(serial_ports)


def read_data(i):
    for port_index, ser in enumerate(ser_ports):
        try:
            # Read data from the Arduino
            data = ser.readline().decode('utf-8').strip()
            if data:
                print(
                    f"Received data from port {serial_ports[port_index]}: {data}")

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

                    temperature_data[port_index].append(temperature)
                    humidity_data[port_index].append(humidity)

                    # Write data to the CSV file
                    row = []
                    for i in range(sensor_count):
                        row.append(temperature_data[i][-1])
                        row.append(humidity_data[i][-1])
                    csv_writer.writerow(row)

                    # Update the plot for each port
                    ax1.clear()
                    for i, temp_data in enumerate(temperature_data):
                        ax1.plot(temp_data, 'o-', markersize=2,
                                 label=f'sensor {i+1}')
                    ax1.set_ylabel('Temperature (°C)')
                    ax1.set_title('HTU21D-F sensor', fontsize=10)
                    ax1.legend()

                    ax2.clear()
                    for i, hum_data in enumerate(humidity_data):
                        ax2.plot(hum_data, 'o-', markersize=2,
                                 label=f'sensor {i+1}')
                    ax2.set_xlabel('Time (s)')
                    ax2.set_ylabel('Relative Humidity (%)')
                    ax2.legend()
                except ValueError:
                    pass  # Skip lines that can't be converted to float
        except KeyboardInterrupt:
            print("Serial communication stopped.")
            for ser in ser_ports:
                ser.close()
        except Exception as e:
            print(f"Error: {e}")


# Create an animation that updates the plot
ani = FuncAnimation(fig, read_data, interval=50)

# Display the plot
plt.show()

# Close CSV file
csv_file.close()
