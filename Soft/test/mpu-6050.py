#!/usr/bin/env python3
import time
import board
import adafruit_mpu6050


i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
mpu = adafruit_mpu6050.MPU6050(i2c)

while True:
    print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % (mpu.acceleration))
    print("Gyro X:%.2f, Y: %.2f, Z: %.2f rad/s" % (mpu.gyro))
    print("Temperature: %.2f C" % mpu.temperature)
    print("")
    time.sleep(1)
    
# class MPU6050Sensor:
#     def __init__(self):
#         self.i2c = board.I2C()
#         self.mpu = adafruit_mpu6050.MPU6050(self.i2c)
        
#     def get_acceleration(self):
#         return self.mpu.acceleration
        
#     def get_gyro(self):
#         return self.mpu.gyro
        
#     def get_temperature(self):
#         return self.mpu.temperature
    
#     def print_sensor_data(self):
#         print("Acceleration: X:%.2f, Y:%.2f, Z:%.2f m/s^2" % self.get_acceleration())
#         print("Gyro X:%.2f, Y:%.2f, Z:%.2f degrees/s" % self.get_gyro())
#         print("Temperature: %.2f C" % self.get_temperature())
#         print("")

# def main():
#     mpu_sensor = MPU6050Sensor()
#     print("MPU6050 object created")
    
#     try:
#         while True:
#             mpu_sensor.print_sensor_data()
#             time.sleep(1)
#     except KeyboardInterrupt:
#         print("Exiting...")
        
# if __name__ == "__main__":
#     main()
