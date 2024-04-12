#!/usr/bin/env python3
import time
import board
from adafruit_onewire.bus import OneWireBus
from adafruit_ds18x20 import DS18X20

# Initialize one-wire bus on board pin D5.
ow_bus = OneWireBus(board.D5)

# Scan for sensors and grab the first one found.
ds18 = DS18X20(ow_bus, ow_bus.scan()[0])

# Main loop to print the temperature every second.
while True:
    print("Temperature: {0:0.3f}C".format(ds18.temperature))
    time.sleep(1.0)

# class DS18B20:
#     def __init__(self, pin):
#         # Initialize the OneWire bus
#         self.onewire_bus = adafruit_onewire.OneWire(pin)
#         # Initialize the DS18B20 sensor
#         self.ds18b20 = adafruit_ds18x20.DS18X20(self.onewire_bus)

#     def read_temperature(self):
#         # Scan for DS18B20 sensors on the bus
#         sensor_ids = self.ds18b20.scan()
#         if sensor_ids:
#             # Read temperature from the first sensor found
#             self.ds18b20.convert_temp()
#             time.sleep(0.75)
#             temperature = self.ds18b20.read_temp(sensor_ids[0])
#             return temperature
#         else:
#             print("No DS18B20 sensor found!")
#             return None

# # Test script
# def main():
#     ds18b20 = DS18B20(board.D4)  # Assuming DS18B20 sensor is connected to D4 pin
#     try:
#         while True:
#             temperature = ds18b20.read_temperature()
#             if temperature is not None:
#                 print("Temperature: {:.2f} C".format(temperature))
#             print("")
#             time.sleep(1)
#     except KeyboardInterrupt:
#         print("Exiting...")

# if __name__ == "__main__":
#     main()
