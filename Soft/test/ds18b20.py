#!/usr/bin/env python3
import os
import glob
import time

# These tow lines mount the device:
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
base_dir = '/sys/bus/w1/devices/'
# Get all the filenames begin with 28 in the path base_dir.
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
def read_rom():
	name_file=device_folder+'/name'
	f = open(name_file,'r')
	return f.readline()
 
def read_temp_raw():
	f = open(device_file, 'r')
	lines = f.readlines()
	f.close()
	return lines
 
def read_temp():
	lines = read_temp_raw()
	# Analyze if the last 3 characters are 'YES'.
	while lines[0].strip()[-3:] != 'YES':
		time.sleep(0.2)
		lines = read_temp_raw()
	# Find the index of 't=' in a string.
	equals_pos = lines[1].find('t=')
	if equals_pos != -1:
		# Read the temperature .
		temp_string = lines[1][equals_pos+2:]
		temp_c = float(temp_string) / 1000.0
		temp_f = temp_c * 9.0 / 5.0 + 32.0
		return temp_c, temp_f
 
print(' rom: '+ read_rom())
while True:
	print(' C=%3.3f  F=%3.3f'% read_temp())
	time.sleep(1)

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
