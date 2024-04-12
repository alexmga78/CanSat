#!/usr/bin/env python3
import time
import RPi.GPIO as GPIO

class MQ9:
    def __init__(self, charge_pin, measure_pin):
        self.charge_pin = charge_pin
        self.measure_pin = measure_pin
        GPIO.setmode(GPIO.BCM)
        # GPIO.setup(self.charge_pin, GPIO.OUT)
        # GPIO.setup(self.measure_pin, GPIO.IN)

    def discharge(self):
        GPIO.setup(self.charge_pin, GPIO.IN)
        GPIO.setup(self.measure_pin, GPIO.OUT)
        GPIO.output(self.measure_pin, False)
        time.sleep(0.005)

    def charge_time(self):
        GPIO.setup(self.measure_pin, GPIO.IN)
        GPIO.setup(self.charge_pin, GPIO.OUT)
        count = 0
        GPIO.output(self.charge_pin, True)
        while not GPIO.input(self.measure_pin):
            count += 1
        return count

    def analog_read(self):
        self.discharge()
        return self.charge_time()

# Test script
def main():
    mq9 = MQ9(charge_pin=18, measure_pin=23)  # Assuming charge pin is GPIO 18 and measure pin is GPIO 23
    try:
        while True:
            print(mq9.analog_read())
            time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting...")
        GPIO.cleanup()

if __name__ == "__main__":
    main()
