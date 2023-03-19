from PyQt5.QtWidgets import QApplication,QWidget
import sys
from GUI.window1 import window1_manager

class GUI_manager():
    def __init__(self):
        self.app = QApplication(sys.argv)
        
        self.window1 = window1_manager()
        
        self.window1.show()
        sys.exit(self.app.exec_())