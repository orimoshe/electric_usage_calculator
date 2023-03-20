from PyQt5.QtWidgets import QApplication,QWidget
import sys
from GUI.window1 import window1_manager
from PyQt5.QtGui import QFont

class GUI_manager():
    def __init__(self):
        self.app = QApplication(sys.argv)
        
        custom_font = QFont()
        custom_font.setPointSize(18)
        self.app.setFont(custom_font)
        
        self.window1 = window1_manager()
        
        self.window1.show()
        sys.exit(self.app.exec_())