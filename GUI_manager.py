import sys

from PyQt5.QtWidgets import QApplication, QWidget

class GUI_manager():
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.root = QWidget()
        self.root.resize(300,300)
        self.root.setWindowTitle("Guru99")
        self.root.show()
        sys.exit(self.app.exec_())