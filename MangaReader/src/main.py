import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtCore import QSize, Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("El's")
        self.setMinimumSize(1000, 550)
        self.button_is_checked = False

        self.button = QPushButton("Push Me!")
        self.button.setCheckable(True)
        self.button.released.connect(self.this_button_was_released)
        self.button.setChecked(self.button_is_checked)

        self.setCentralWidget(self.button)

    def this_button_was_released(self):
        self.button_is_checked = self.button.isChecked()

        print(self.button_is_checked)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()