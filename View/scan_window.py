from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

def button_pressed():
    print("Button has been pressed")

app = QApplication([])
win = QMainWindow()
button = QPushButton("Click Me", win)

button.clicked.connect(button_pressed)

win.show()

app.exec()