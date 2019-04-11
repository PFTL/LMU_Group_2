import numpy as np
import yaml
from Model.analog_daq import AnalogDaq

import pint
ur = pint.UnitRegistry()

class Experiment:
    def load_config(self, filename):
        with open(filename, 'r') as f:
            self.params = yaml.load(f)

    def load_daq(self):
        port = self.params['DAQ']['port']
        resistance = self.params['DAQ']['resistance']

        self.daq = AnalogDaq(port, resistance)
        self.daq.initialize()

    def do_scan(self):
        start = ur(self.params['Scan']['start'])
        stop = ur(self.params['Scan']['stop'])
        step = ur(self.params['Scan']['step'])

        self.voltages = np.arange(start.m_as('V'), stop.m_as('V')+step.m_as('V'), step.m_as('V'))
        self.currents = np.zeros((len(self.voltages)))

        channel_out = self.params['Scan']['channel_out']
        channel_in = self.params['Scan']['channel_in']
        for i in range(len(self.voltages)):
            volt = self.voltages[i]
            self.daq.set_voltage(channel_out, volt*ur('V'))
            self.currents[i] = self.daq.read_current(channel_in).m_as('A')

    def save_data(self, filename):
        np.savetxt(filename, [self.voltages, self.currents])

    def save_metadata(self, filename):
        with open(filename, 'w') as f:
            yaml.dump(self.params, f)

    def finish(self):
        pass


if __name__ == "__main__":
    exp = Experiment()
    exp.load_config('config.txt')