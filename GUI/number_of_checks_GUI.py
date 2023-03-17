from PyQt5.QtWidgets import QApplication,QLineEdit,QWidget,QFormLayout, QPushButton, QVBoxLayout
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QFont
from PyQt5.QtCore import Qt
import global_variables as g

class input_GUI(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)

        self.e2 = []
        
        self.e3 = QLineEdit()
        self.e3.setValidator(QDoubleValidator())

        self.e4 = QLineEdit()
        self.e4.setValidator(QDoubleValidator())

        self.e5 = QLineEdit()
        self.e5.setValidator(QDoubleValidator())

        self.e6 = QLineEdit()
        self.e6.setValidator(QDoubleValidator())

        self.e7 = QLineEdit()
        self.e7.setValidator(QDoubleValidator())

        sumbitButton = QPushButton("Submit")
        
        get_number_of_checks(self)
        
        flo = QFormLayout()
        
        for check in range(int(self.e1.text())):
            self.e2.append(QLineEdit())
            self.e2[check].setValidator(QDoubleValidator())
            name_of_title = "NUMBER_OF_WATS_IN_CHECK " + str(check) 
            flo.addRow("NUMBER_OF_WATS_IN_CHECK",self.e2[check])
        
        #TODO: NUMBER_OF_WATS_IN_CHECK need to be arr size of NUMBER_OF_CHECKS
        
        sumbitButton.clicked.connect(self.button_click)
        
        flo.addRow("PRICES_OF_WATS_IN_CHECK",self.e3)
        flo.addRow("SERVICE_TAXES",self.e4)
        flo.addRow("LAST_WATS_OF_SMALL_APARTMENT",self.e5)
        flo.addRow("WATS_OF_SMALL_APARTMENT_NOW",self.e6)
        flo.addRow("WATS_OF_BOTH_APARTMENTS",self.e7)
        flo.addRow(sumbitButton)
        

        self.setLayout(flo)
  

    def button_click(self, layout):
        
        if layout == g.NUMBER_OF_CHECKS_LAYOUT:
            g.NUMBER_OF_CHECKS = int(self.e1.text())
        else:
            inizialize_variables_from_user(self)


def get_number_of_checks(self):
    self.e1 = QLineEdit()
    self.e1.setValidator(QIntValidator())
    self.e1.setFont(QFont("Arial",20))
    self.e1.setText('1')
    
    get_number_of_checks_button = QPushButton("Submit")
    get_number_of_checks_button.clicked.connect(self.button_click, g.NUMBER_OF_CHECKS_LAYOUT)

    get_number_of_checks_layout = QFormLayout()
    get_number_of_checks_layout.addRow("NUMBER_OF_CHECKS",self.e1)
    get_number_of_checks_layout.addRow(get_number_of_checks_button)
    
    
    self.setLayout(get_number_of_checks_layout)
    
def inizialize_variables_from_user(self):
    print(self.e1.text())
    