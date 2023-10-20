#include <Arduino.h>
#include <Wire.h>
#include "Adafruit_HTU21DF.h"

Adafruit_HTU21DF htu = Adafruit_HTU21DF();
const int externalLedPin = 8; // Define the pin where the external LED is connected
const int builtInLedPin = 13; // Define the pin for the built-in LED

void setup() {
  Serial.begin(9600);
  Serial.println("HTU21D-F test");

  if (!htu.begin()) {
    Serial.println("Couldn't find sensor!");
    while (1);
  }

  pinMode(externalLedPin, OUTPUT); // Set the external LED pin as an output
  pinMode(builtInLedPin, OUTPUT);   // Set the built-in LED pin as an output
}

void loop() {
    float temp = htu.readTemperature();
    float rel_hum = htu.readHumidity();
    Serial.print("Temp: "); Serial.print(temp); Serial.print(" C");
    Serial.print("\t\t");
    Serial.print("Humidity: "); Serial.print(rel_hum); Serial.println(" %");

    digitalWrite(externalLedPin, HIGH); // Turn on the external LED
    digitalWrite(builtInLedPin, HIGH);   // Turn on the built-in LED
    delay(100); // Keep the LEDs on for 100 milliseconds
    digitalWrite(externalLedPin, LOW); // Turn off the external LED
    digitalWrite(builtInLedPin, LOW);   // Turn off the built-in LED
    delay(400); // Wait for 400 milliseconds before the next reading
}
