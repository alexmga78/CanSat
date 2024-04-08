#!/usr/bin/env python3
import time
import board
import adafruit_bmp3xx

class BMP388:
    def __init__(self):
        # Initialize I2C bus and BMP388 sensor
        self.i2c = board.I2C()
        self.bmp388 = adafruit_bmp3xx.BMP3XX_I2C(self.i2c)

    def read_temperature(self):
        # Read temperature from BMP388 sensor
        return self.bmp388.temperature

    def read_pressure(self):
        # Read pressure from BMP388 sensor
        return self.bmp388.pressure

    def read_altitude(self):
        # Read altitude from BMP388 sensor
        return self.bmp388.altitude

# Test script
def main():
    bmp = BMP388()
    try:
        while True:
            temperature = bmp.read_temperature()
            pressure = bmp.read_pressure()
            altitude = bmp.read_altitude()

            print("Temperature: {:.2f} C".format(temperature))
            print("Pressure: {:.2f} hPa".format(pressure / 100))
            print("Altitude: {:.2f} meters".format(altitude))
            print("")

            time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting...")

if __name__ == "__main__":
    main()
