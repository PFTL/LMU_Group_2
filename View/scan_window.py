from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5 import uic
import os
import threading

class ScanWindow(QMainWindow):
    def __init__(self, experiment):
        super().__init__()

        self.experiment = experiment
        this_dir = os.path.dirname(os.path.abspath(__file__))
        scan_file = os.path.join(this_dir, 'scan_window.ui')
        uic.loadUi(scan_file, self)

        self.start_button.clicked.connect(self.start_pressed)
        self.stop_button.clicked.connect(self.stop_pressed)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_start_button)
        self.timer.start(100)  # In milliseconds

    def update_start_button(self):
        if self.experiment.scan_running:
            self.start_button.setEnabled(False)
        else:
            self.start_button.setEnabled(True)

    def start_pressed(self):
        t = threading.Thread(target=self.experiment.do_scan)
        t.start()
        self.start_button.setEnabled(False)

    def stop_pressed(self):
        self.experiment.stop_scan = True

if __name__ == "__main__":
    app = QApplication([])
    win = ScanWindow()
    win.show()
    app.exec()