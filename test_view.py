from PyQt5.QtWidgets import QApplication
from Model.IV_Measurement import Experiment
from View.scan_window import ScanWindow

exp = Experiment()
exp.load_config('Config/experiment.yml')
exp.load_daq()

app = QApplication([])
scan_win = ScanWindow(exp)
scan_win.show()
app.exec()