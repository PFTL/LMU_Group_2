from Controller.simple_daq import SimpleDaq

import pint

ur = pint.UnitRegistry()

class AnalogDaq:
    def __init__(self, port, resistance):
        self.port = port
        self.resistance = ur(resistance)

    def initialize(self):
        self.driver = SimpleDaq(self.port)

    def set_voltage(self, channel, voltage):
        voltage = voltage.m_as('V')
        voltage_int = int(voltage/3.3*4095)
        self.driver.set_analog_value(channel, voltage_int)

    def read_current(self, channel):
        voltage = self.driver.get_analog_value(channel)
        voltage_volts = voltage/1023*ur('3.3V')
        current = voltage_volts/self.resistance
        self.current = current
        return current

    def finish(self):
        pass


if __name__ == "__main__":
    resistance = ur('100ohm')
    dev = AnalogDaq('/dev/ttyACM0', resistance)
    dev.initialize()
    dev.set_voltage(0, ur('3.3V'))
    current = dev.read_current(0)
    print('The current is {}'.format(current.to('mA')))
    print('Other things')
    print('The current is {}'.format(dev.current.to('mA')))

