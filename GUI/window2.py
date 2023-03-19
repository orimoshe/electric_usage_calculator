from Utils.imports import *
import Utils.utils as utils 
import Utils.prints as prints

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
        info_parameters = ["start_date", "end_date","change_price_date", "number_of_wats_in_check", "prices_of_wats_in_check", "wats_of_small_apartment_now", "wats_of_both_apartments", \
                            "last_wats_of_small_apartment", "service_tax"]
        self.info = {}
            
        for parameter in info_parameters:
            if(parameter == "change_price_date" or parameter == "number_of_wats_in_check" or \
                parameter == "prices_of_wats_in_check"):
                for check in range(self.number_of_checks):
                    item_name = parameter + "_" + str(check)
                    
                    self.info[item_name] = QLineEdit()            
                    self.info[item_name].setValidator(QDoubleValidator())
            else:
                item_name = parameter
                self.info[item_name] = QLineEdit()            
                self.info[item_name].setValidator(QDoubleValidator())

        for item_name, item_value in self.info.items():
            self.add_number_of_wats_row(item_name, item_value)

        self.layout.addRow("Button2", self.sumbitButton2)
        
    def add_number_of_wats_row(self, item_name, item_value):
            self.layout.addRow(item_name, item_value)
        
    def button_click2(self, a, b):
        utils.get_user_inputs(self)

        
        self.calculate_data()
        
    def calculate_data(self):
        precentage_of_wats_in_check = utils.calculate_precentage_of_wats_in_check()    
        wats_of_small_apartment_in_all_checks = utils.calculate_wats_of_small_apartment_in_all_checks()   
        cost_of_wats_in_check = utils.calculate_cost_of_wats_in_check(precentage_of_wats_in_check, wats_of_small_apartment_in_all_checks)
        total_cost_of_wats_in_checks_before_taxes = utils.calculate_total_cost_of_wats_in_checks_before_taxes(cost_of_wats_in_check)

        total_cost_of_wats_in_checks_after_taxes = utils.calculate_total_cost_of_wats_in_checks_after_taxes(total_cost_of_wats_in_checks_before_taxes)
        
        
        prints.base_data(self)
        
        
        print("total pay of small apartment " + str(total_cost_of_wats_in_checks_after_taxes))