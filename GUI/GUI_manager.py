from PyQt5.QtWidgets import QApplication,QWidget
import sys
from GUI.window1 import window1_manager

class GUI_manager():
    def __init__(self):
        #create app
        self.app = QApplication(sys.argv)
        
        #create window 1
        self.window1 = QWidget()
        self.window1.resize(440,240)
        self.window1.setWindowTitle("electric usage calculator")
        window1_manager(self.window1)
        
        self.window1.show()
        sys.exit(self.app.exec_())
        
def close_window(self):
    self.close()