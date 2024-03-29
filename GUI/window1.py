from GUI.window2 import window2_manager
from Utils.imports import *
from Utils.Bill import *

class window1_manager(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.create_window1()
        self.get_input_from_user()
      
    def create_window1(self):
        self.window1 = QWidget()
        self.window1.resize(260,100)
        self.window1.setWindowTitle("electric usage calculator")  
    
    def get_input_from_user(self):
        self.create_input_lines()
        self.create_and_connect_sumbit_button()
        self.create_layout()
        
    def create_input_lines(self):
        self.number_of_checks = self.create_double_line_edit()
        self.service_taxes = self.create_double_line_edit()
        self.last_wats_of_small_apartment_lineEdit = self.create_double_line_edit()
        self.wats_of_small_apartment_now_lineEdit = self.create_double_line_edit()
        self.wats_of_both_apartments_lineEdit = self.create_double_line_edit()
        self.start_date_lineEdit = self.create_double_line_edit()
        self.end_date_lineEdit = self.create_double_line_edit()
        
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

        last_wats_of_small_apartment_name = QLabel()
        last_wats_of_small_apartment_name.setText("קריאת הוואט הקודמת בדירה הקטנה") 
        
        wats_of_small_apartment_now_name = QLabel()
        wats_of_small_apartment_now_name.setText("צריכת הוואט בדירה הקטנה עכשיו") 
        
        wats_of_both_apartments_name = QLabel()
        wats_of_both_apartments_name.setText("צריכת הוואט בשתי הדירות")
        
        start_date_name = QLabel()
        start_date_name.setText("תאריך תחילת החשבון")
        
        end_date_name = QLabel()
        end_date_name.setText("תאריך סוף החשבון")
        
        
        self.layout.addWidget(self.number_of_checks, 0, 0)
        self.layout.addWidget(number_of_checks_name, 0, 1)
        
        self.layout.addWidget(self.service_taxes, 1, 0)
        self.layout.addWidget(service_taxes_name, 1, 1)

        self.layout.addWidget(self.last_wats_of_small_apartment_lineEdit, 2, 0)
        self.layout.addWidget(last_wats_of_small_apartment_name, 2, 1)

        self.layout.addWidget(self.wats_of_small_apartment_now_lineEdit, 3, 0)
        self.layout.addWidget(wats_of_small_apartment_now_name, 3, 1)

        self.layout.addWidget(self.wats_of_both_apartments_lineEdit, 4, 0)
        self.layout.addWidget(wats_of_both_apartments_name, 4, 1)

        self.layout.addWidget(self.start_date_lineEdit, 5, 0)
        self.layout.addWidget(start_date_name, 5, 1)

        self.layout.addWidget(self.end_date_lineEdit, 6, 0)
        self.layout.addWidget(end_date_name, 6, 1)


        self.layout.addWidget(self.sumbitButton1, 7, 0)
        
        self.setLayout(self.layout)

    def create_bill_info(self):
        self.bill_info = Bill(
            NUMBER_OF_CHECKS = int(self.number_of_checks.text()), 
            SERVICE_TAXES = float(self.service_taxes.text()),
            LAST_WATS_OF_SMALL_APARTMENT = float(self.last_wats_of_small_apartment_lineEdit.text()),
            WATS_OF_SMALL_APARTMENT_NOW = float(self.wats_of_small_apartment_now_lineEdit.text()),
            WATS_OF_BOTH_APARTMENTS = float(self.wats_of_both_apartments_lineEdit.text()),
            START_DATE = float(self.start_date_lineEdit.text()),
            END_DATE = float(self.end_date_lineEdit.text())
            )
    
    def button_click1(self, a,b):
        self.create_bill_info()
        window2_instance = window2_manager(self.bill_info)
        window2_instance.window2.show()