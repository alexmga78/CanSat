#!/usr/bin/env python3
import time
import board
import analogio

class MQ9:
    def __init__(self, pin):
        # Initialize analog input pin
        self.analog_in = analogio.AnalogIn(pin)

    def read_raw_value(self):
        # Read raw sensor value (ADC counts)
        return self.analog_in.value

    def read_voltage(self):
        # Read sensor voltage
        return (self.analog_in.value * 3.3) / 65536

    def read_gas_concentration(self):
        # Read gas concentration (replace with your calibration logic)
        # Example: map raw value to gas concentration based on calibration curve
        raw_value = self.read_raw_value()
        # Example calibration curve: gas_concentration = a * raw_value + b
        a = 0.1  # Example calibration parameter
        b = 10   # Example calibration parameter
        gas_concentration = a * raw_value + b
        return gas_concentration

# Test script
def main():
    mq9 = MQ9(board.A1)  # Assuming MQ-9 sensor is connected to A1 pin
    try:
        while True:
            raw_value = mq9.read_raw_value()
            voltage = mq9.read_voltage()
            gas_concentration = mq9.read_gas_concentration()

            print("Raw Value: {}".format(raw_value))
            print("Voltage: {:.2f} V".format(voltage))
            print("Gas Concentration: {:.2f} ppm".format(gas_concentration))
            print("")

            time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting...")

if __name__ == "__main__":
    main()
