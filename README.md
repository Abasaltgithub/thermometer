# HTU21D-F Temperature and Humidity Sensor with Arduino


This repository contains the code and documentation for interfacing the HTU21D-F temperature and humidity sensor with an Arduino. With this project, you can read temperature and humidity data from the sensor and use it for various applications.

## Table of Contents

- [Introduction](#introduction)
- [Hardware Requirements](#hardware-requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The HTU21D-F Temperature + Humidity Sensor is a precise and intelligent I2C digital humidity sensor. It offers accurate humidity measurements with typical accuracy within ±2% over a range of 5% to 95% relative humidity. Temperature measurements are accurate within ±1°C from -30°C to 90°C. The breakout board includes a PTFE filter for sensor protection, a 3.3V regulator, and I2C level shifting circuitry, making it compatible with microcontrollers operating at 3.3V to 5V. The STEMMA QT form factor and connectors allow easy interfacing, and it can be used with SparkFun Qwiic I2C connectors. Each order includes a fully assembled PCB breakout and header, which requires soldering for use in a breadboard.

## Hardware Requirements

To get started with this project, you will need the following hardware:

- HTU21D-F Temperature and Humidity Sensor
- Arduino board (e.g., Arduino Uno)
- Jumper wires
- Breadboard (optional)

## Installation

1. **Wiring**: Connect the HTU21D-F sensor to your Arduino board using jumper wires. Make sure to connect the VCC, GND, SDA, and SCL pins correctly. You can refer to the datasheet or the provided example wiring diagram for guidance.

2. **Arduino IDE**: Ensure you have the Arduino IDE installed on your computer. If not, download and install it from the [Arduino website](https://www.arduino.cc/en/software).

3. **Library Installation**: Install the HTU21D-F sensor library for Arduino. You can do this via the Arduino Library Manager. Open the Arduino IDE, go to `Sketch > Include Library > Manage Libraries`, search for "HTU21D-F," and click "Install."

4. **Upload Code**: Open the Arduino IDE and load the example sketch provided in this repository (`htu21d_example.ino`). Upload the code to your Arduino board.

## Usage

1. After uploading the code to your Arduino, open the Serial Monitor (under `Tools > Serial Monitor`) in the Arduino IDE.

2. Set the baud rate in the Serial Monitor to the same value specified in the Arduino code (typically 9600 baud).

3. The sensor will start reading temperature and humidity data and display it in the Serial Monitor.

4. You can use this data for your specific project or modify the code to suit your needs.

## Contributing

If you'd like to contribute to this project, please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with clear, concise commit messages.
4. Push your changes to your fork.
5. Create a pull request with a detailed description of your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Feel free to reach out with any questions or issues related to this project. Enjoy working with the HTU21D-F sensor and Arduino!
