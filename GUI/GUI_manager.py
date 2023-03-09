from PyQt5.QtWidgets import QApplication,QLineEdit,QWidget,QFormLayout, QPushButton, QVBoxLayout
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QFont
from PyQt5.QtCore import Qt
import sys

from GUI.number_of_checks_GUI import input_GUI

class GUI_manager():
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.root = QWidget()
        
        self.root.resize(440,240)
        self.root.setWindowTitle("electric usage calculator")
        
        input_GUI(self.root)
        
        self.root.show()
        sys.exit(self.app.exec_())

def close_window(self):
    self.close()