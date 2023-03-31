from Utils.imports import *
import Utils.utils as utils 
import Utils.prints as prints
import Utils.global_variables as g
from Utils.Bill import *

class window2_manager():
    def __init__(self, bill_info, parent=None):
        super().__init__()
        
        self.bill_info = bill_info
        self.create_complete_input_window()
    
    def create_complete_input_window(self):
        self.create_widget()
        self.create_and_connect_sumbit_button()
        self.create_layout()
                
    def create_widget(self):
        self.window2 = QWidget()
        self.window2.setWindowTitle("electric usage calculator")
        
        self.widget = QWidget()
        self.textLabel = QLabel(self.widget)


    def create_and_connect_sumbit_button(self):
        self.sumbitButton2 = QPushButton("Submit2")
        self.sumbitButton2.clicked.connect(partial(self.button_click2, self))

    def create_layout(self):
        self.layout = QGridLayout()
        self.add_rows_to_layout()
        self.window2.setLayout(self.layout)

    def add_rows_to_layout(self):
        self.info = {}
        for input_name in self.bill_info.INPUT_NAMES:
            if(input_name == "תאריך שינוי המחיר" or input_name == "כמות הוואט בחשבון" or \
                input_name == "מחיר הוואט בחשבון"):
                for check in range(self.bill_info.NUMBER_OF_CHECKS):
                    item_name = input_name + " " + str(check+1)
                    self.initialize_input_value(item_name)
            else:
                item_name = input_name    
                self.initialize_input_value(item_name)
        row=0
        for item_name, item_value in self.info.items():
            self.add_number_of_wats_row(item_name, item_value, row)
            row+=1
            
        self.layout.addWidget(self.sumbitButton2, len(self.info.items()) + 1, 0)
        
    def initialize_input_value(self, item_name):
        self.info[item_name] = QLineEdit()            
        self.info[item_name].setAlignment(QtCore.Qt.AlignRight)
        self.info[item_name].setValidator(QDoubleValidator())
        
    def add_number_of_wats_row(self, item_name, item_value, row):
        info_label = QLabel()
        info_label.setText(item_name) 
        
        self.layout.addWidget(item_value, row, 0)
        self.layout.addWidget(info_label, row, 1)


    def button_click2(self, a, b):
        utils.get_user_inputs(self)
        self.calculate_data()
        
    def calculate_data(self):
        precentage_of_wats_in_check = utils.calculate_precentage_of_wats_in_check(self)    
        wats_of_small_apartment_in_all_checks = utils.calculate_wats_of_small_apartment_in_all_checks()
           
        #TODO: dont pass argument, have a global variable for that
        cost_of_wats_in_check = utils.calculate_cost_of_wats_in_check(self, precentage_of_wats_in_check, wats_of_small_apartment_in_all_checks)
        total_cost_of_wats_in_checks_before_taxes = utils.calculate_total_cost_of_wats_in_checks_before_taxes(cost_of_wats_in_check)

        total_cost_of_wats_in_checks_after_taxes = utils.calculate_total_cost_of_wats_in_checks_after_taxes(self, total_cost_of_wats_in_checks_before_taxes)
        
        
        prints.base_data(self)