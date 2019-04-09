import pint
import serial
import time

ur = pint.UnitRegistry()


class Device:
    def __init__(self, port):
        self.rsc = serial.Serial(port)
        self.rsc=serial.Serial(port)
        time.sleep(1)

    def set_voltage(self, channel, voltage):
        voltage_v = voltage.m_as('V')
        voltage_i = int(voltage_v/3.3*4095)
        command = 'OUT:CH{}:{}'.format(channel, voltage_i)
        self.write(command)
        time.sleep(0.05)

    def read_voltage(self, channel):
        command = 'IN:CH{}'.format(channel)
        voltage = self.query(command)
        voltage = int(voltage)
        voltage = voltage/1023*ur('3.3V')
        current = voltage/ur('220ohm')
        return current.to('mA')

    def idn(self):
        answer = self.query('IDN')
        return answer

    def query(self, command):
        self.write(command)
        return self.read()

    def read(self):
        message = self.rsc.readline()
        message = message.strip()
        message = message.decode()
        return message

    def write(self, command):
        command = command + '\n'
        command = command.encode('utf-8')
        self.rsc.write(command)

    def finalize(self):
        pass


dev = Device('/dev/ttyACM0')
print(dev.idn())
dev.set_voltage(0, ur('3.3V'))
dev.set_voltage(0, ur('3.29V'))
current = dev.read_voltage(0)
print('Measured current: {}'.format(current))

# voltages = [i for i in range(4095) if i%50==0]
# currents = []
#
# for v in voltages:
#     dev.set_voltage(0, v)
#     current = dev.read_voltage(0)
#     currents.append(current)
#
# print(currents)
