from GUI.window2 import window2_manager
from Utils.imports import *
class window1_manager(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.create_widget()
        self.get_number_of_checks_from_user()
      
    def create_widget(self):
        self.window1 = QWidget()
        self.window1.resize(260,100)
        self.window1.setWindowTitle("electric usage calculator")  
    
    def get_number_of_checks_from_user(self):
        self.create_number_of_checks()
        self.create_and_connect_sumbit_button()
        self.create_layout()
        
    def create_number_of_checks(self):
        self.number_of_checks = QLineEdit()
        self.number_of_checks.setAlignment(QtCore.Qt.AlignRight)
        self.number_of_checks.setValidator(QDoubleValidator())
    
    def create_and_connect_sumbit_button(self):
        self.sumbitButton1 = QPushButton("לחץ")
        self.sumbitButton1.clicked.connect(partial(self.button_click1, self))
    
    def create_layout(self):
        self.layout = QHBoxLayout()
        
        top_label = QLabel()
        top_label.setText("כמות התעריפים") 
        
        self.layout.addWidget(self.sumbitButton1)
        self.layout.addWidget(self.number_of_checks)
        self.layout.addWidget(top_label)
        self.setLayout(self.layout)

    def button_click1(self, a,b):
        window2_instance = window2_manager(self.number_of_checks)
        window2_instance.window2.show()