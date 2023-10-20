import serial

# Define the serial port and baud rate (make sure they match your Arduino settings)
# Replace 'COM3' with your Arduino's serial port
ser = serial.Serial('/dev/tty.usbserial-2110', 9600)

try:
    while True:
        # Read data from the Arduino
        data = ser.readline().decode('utf-8').strip()
        print(data)

except KeyboardInterrupt:
    print("Serial communication stopped.")

finally:
    ser.close()
