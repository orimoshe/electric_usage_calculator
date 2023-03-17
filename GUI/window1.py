from PyQt5.QtWidgets import QLineEdit,QWidget,QFormLayout, QPushButton
from PyQt5.QtGui import QDoubleValidator
from GUI.window2 import window2_manager
from functools import partial

class window1_manager(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        
        self.get_number_of_checks_from_user()
        
    def get_number_of_checks_from_user(self):
        self.create_number_of_checks()
        self.create_and_connect_sumbit_button()
        self.create_layout()
        
    def create_number_of_checks(self):
        self.number_of_checks = QLineEdit()
        self.number_of_checks.setValidator(QDoubleValidator())
    
    def create_and_connect_sumbit_button(self):
        self.sumbitButton1 = QPushButton("Submit1")
        self.sumbitButton1.clicked.connect(partial(self.button_click1, self))
    
    def create_layout(self):
        self.layout = QFormLayout()
        self.layout.addRow("number_of_checks", self.number_of_checks)
        self.layout.addRow("Button1", self.sumbitButton1)
        self.setLayout(self.layout)

    def button_click1(self, a,b):
        print(self.number_of_checks.text())
        
        window2_instance = window2_manager(self.number_of_checks)
        window2_instance.window2.show()