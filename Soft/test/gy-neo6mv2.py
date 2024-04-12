#!/usr/bin/env python3
# import time
# import serial

# class GYNEO6MV2:
#     def __init__(self, port, baudrate=9600):
#         # Initialize UART communication
#         self.ser = serial.Serial(port, baudrate)

#     def read_data(self):
#         # Read data from GPS module
#         data = self.ser.readline().decode().strip()
#         return data

# # Test script
# def main():
#     gps = GYNEO6MV2("/dev/ttyS0")  # Assuming GPS module is connected to UART port ttyAMA0
#     try:
#         while True:
#             gps_data = gps.read_data()
#             print("GPS Data: {}".format(gps_data))
#             time.sleep(1)
#     except KeyboardInterrupt:
#         print("Exiting...")

# if __name__ == "__main__":
#     main()


import serial
from time import sleep
import sys

ser = serial.Serial ("/dev/ttyAMA0")
print(ser)
try:
	print("@@@@")
	while True:
		data = (str)(ser.readline())
		print("??")
		print(data, "\n")
except KeyboardInterrupt:
	print("Exiting...")
	sys.exit(0)