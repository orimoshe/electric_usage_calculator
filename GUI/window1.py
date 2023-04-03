from GUI.window2 import window2_manager
from Utils.imports import *
from Utils.Bill import *

class window1_manager(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.create_widget()
        self.get_input_from_user()
      
    def create_widget(self):
        self.window1 = QWidget()
        self.window1.resize(260,100)
        self.window1.setWindowTitle("electric usage calculator")  
    
    def get_input_from_user(self):
        self.create_input_lines()
        self.create_and_connect_sumbit_button()
        self.create_layout()
        
    def create_input_lines(self):
        #make variables local and not self
        self.number_of_checks = self.create_double_line_edit()
        self.service_taxes = self.create_double_line_edit()
        
    def create_double_line_edit(self):
        double_line_edit = QLineEdit()
        double_line_edit.setAlignment(QtCore.Qt.AlignRight)
        double_line_edit.setValidator(QDoubleValidator())
        return double_line_edit
    
    def create_and_connect_sumbit_button(self):
        self.sumbitButton1 = QPushButton("לחץ")
        self.sumbitButton1.clicked.connect(partial(self.button_click1, self))
    
    def create_layout(self):
        self.layout = QGridLayout()
        
        number_of_checks_name = QLabel()
        number_of_checks_name.setText("כמות התעריפים") 
        
        service_taxes_name = QLabel()
        service_taxes_name.setText("תשלום קבוע") 
        
        self.layout.addWidget(self.number_of_checks, 0, 0)
        self.layout.addWidget(number_of_checks_name, 0, 1)
        
        self.layout.addWidget(self.service_taxes, 1, 0)
        self.layout.addWidget(service_taxes_name, 1, 1)

        self.layout.addWidget(self.sumbitButton1, 2, 0)
        
        self.setLayout(self.layout)

    def create_bill_info(self):
        self.bill_info = Bill(NUMBER_OF_CHECKS = int(self.number_of_checks.text()), SERVICE_TAXES = float(self.service_taxes.text()))
    
    def button_click1(self, a,b):
        self.create_bill_info()
        window2_instance = window2_manager(self.bill_info)
        window2_instance.window2.show()