from PyQt5.QtWidgets import QLineEdit,QWidget,QFormLayout, QPushButton
from PyQt5.QtGui import QDoubleValidator
from functools import partial

class window2_manager():
    def __init__(self, number_of_checks, parent=None):
        super().__init__()        
        self.number_of_checks = int(number_of_checks.text())
        self.create_complete_input_window()
    
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
        self.layout = QFormLayout()
        self.add_rows_to_layout()
        self.window2.setLayout(self.layout)

    def add_rows_to_layout(self):
        info_parameters = ["number_of_wats_in_check", "wats_of_small_apartment_now", "wats_of_both_apartments", \
                            "last_wats_of_small_apartment", "prices_of_wats_in_check", "service_tax"]
        self.info = {}
            
        for parameter in info_parameters:
            if(parameter == "service_tax"):
                item_name = parameter
                
                self.info[item_name] = QLineEdit()            
                self.info[item_name].setValidator(QDoubleValidator())
            else:
                for check in range(self.number_of_checks):
                    item_name = parameter + "_" + str(check)
                    
                    self.info[item_name] = QLineEdit()            
                    self.info[item_name].setValidator(QDoubleValidator())


        for item_name, item_value in self.info.items():
            self.add_number_of_wats_row(item_name, item_value)

        self.layout.addRow("Button2", self.sumbitButton2)
        
    def add_number_of_wats_row(self, item_name, item_value):
            self.layout.addRow(item_name, item_value) 
        
    def button_click2(self, a, b):
        self.debug_print()

    def debug_print(self):
        input_values = self.info.values()
        for value in input_values:
            print(value.text())
        