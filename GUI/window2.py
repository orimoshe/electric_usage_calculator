from PyQt5.QtWidgets import QLineEdit,QWidget,QFormLayout, QPushButton
from PyQt5.QtGui import QDoubleValidator
from functools import partial

class window2_manager():
    def __init__(self, number_of_checks, parent=None):
        super().__init__()
        
        print("init2")
        
        self.number_of_checks = int(number_of_checks.text())
        self.create_complete_input_window()
        
        print("end init2")
    
    def create_complete_input_window(self):
        self.create_widget()
        self.create_and_connect_sumbit_button()
        self.create_layout()
                
    def create_widget(self):
        self.window2 = QWidget()
        self.window2.setWindowTitle("electric usage calculator")
        
    def create_and_connect_sumbit_button(self):
        self.sumbitButton2 = QPushButton("Submit2")
        self.sumbitButton2.clicked.connect(partial(self.button_click2, self))

    def create_layout(self):
        self.number_of_wats_in_check = []
        self.layout = QFormLayout()
        
        self.add_rows_to_layout()
        
        self.window2.setLayout(self.layout)

    def add_rows_to_layout(self):
        self.add_number_of_wats_row()

        self.layout.addRow("Button2", self.sumbitButton2)
        
    def add_number_of_wats_row(self):
        for check in range(self.number_of_checks):
            self.number_of_wats_in_check.append(QLineEdit())
            self.number_of_wats_in_check[check].setValidator(QDoubleValidator())
                
            self.layout.addRow("number_of_wats_in_check " + str(check), self.number_of_wats_in_check[check])        
        
    def button_click2(self, a, b):
        for i in range(0, len(self.number_of_wats_in_check)):
            print(self.number_of_wats_in_check[i].text())