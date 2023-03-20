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
        #Window 2 diget
        self.window2 = QWidget()
        self.window2.setWindowTitle("electric usage calculator")
        
        #Output widget
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
        #TODO: parameters out of this function into other file
        info_parameters = ["תאריך התחלת החשבון", "תאריך סוף החשבון","תאריך שינוי המחיר", "כמות הוואט בחשבון",\
            "מחיר הוואט בחשבון", "צריכת הוואט בדירה הקטנה עכשיו", "צריכת הוואט בשתי הדירות", \
                            "קריאת הוואט הקודמת בדירה הקטנה", "תשלום קבוע"]
        self.info = {}
            
        for parameter in info_parameters:
            if(parameter == "תאריך שינוי המחיר" or parameter == "כמות הוואט בחשבון" or \
                parameter == "מחיר הוואט בחשבון"):
                for check in range(self.number_of_checks):
                    item_name = parameter + " " + str(check+1)
                    
                    #TODO: these 3 lines should be a funciton use them below too    
                    self.info[item_name] = QLineEdit()            
                    self.info[item_name].setAlignment(QtCore.Qt.AlignRight)
                    self.info[item_name].setValidator(QDoubleValidator())
            else:
                item_name = parameter

                self.info[item_name] = QLineEdit()            
                self.info[item_name].setAlignment(QtCore.Qt.AlignRight)
                self.info[item_name].setValidator(QDoubleValidator())
        index=0
        for item_name, item_value in self.info.items():
            self.add_number_of_wats_row(item_name, item_value, index)
            index+=1

        #TODO: change sumbitButton2 name and  sumbitButton1 name from window1
        self.layout.addWidget(self.sumbitButton2, len(self.info.items()) + 1, 0)
        
    def add_number_of_wats_row(self, item_name, item_value, index):
        info_label = QLabel()
        info_label.setText(item_name) 
        
        self.layout.addWidget(item_value, index, 0)
        self.layout.addWidget(info_label, index, 1)


    def button_click2(self, a, b):
        utils.get_user_inputs(self)

        
        self.calculate_data()
        
    def calculate_data(self):
        precentage_of_wats_in_check = utils.calculate_precentage_of_wats_in_check()    
        wats_of_small_apartment_in_all_checks = utils.calculate_wats_of_small_apartment_in_all_checks()
           
        #TODO: dont pass argument, have a global variable for that
        cost_of_wats_in_check = utils.calculate_cost_of_wats_in_check(precentage_of_wats_in_check, wats_of_small_apartment_in_all_checks)
        total_cost_of_wats_in_checks_before_taxes = utils.calculate_total_cost_of_wats_in_checks_before_taxes(cost_of_wats_in_check)

        total_cost_of_wats_in_checks_after_taxes = utils.calculate_total_cost_of_wats_in_checks_after_taxes(total_cost_of_wats_in_checks_before_taxes)
        
        
        prints.base_data(self)