# import sys

# from PyQt5.QtWidgets import QApplication, QWidget

from PyQt5.QtWidgets import QApplication,QLineEdit,QWidget,QFormLayout, QPushButton, QVBoxLayout
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QFont
from PyQt5.QtCore import Qt, pyqtSignal
import sys
class lineEdit(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        
        e1 = QLineEdit()
        e1.setValidator(QIntValidator())

        e1.setAlignment(Qt.AlignLeft)
        e1.setFont(QFont("Arial",20))

        e2 = QLineEdit()
        e2.setValidator(QDoubleValidator())
        
        e3 = QLineEdit()
        e3.setValidator(QDoubleValidator())

        e4 = QLineEdit()
        e4.setValidator(QDoubleValidator())

        e5 = QLineEdit()
        e5.setValidator(QDoubleValidator())

        e6 = QLineEdit()
        e6.setValidator(QDoubleValidator())

        e7 = QLineEdit()
        e7.setValidator(QDoubleValidator())

        sumbitButton = QPushButton("Submit")
        # sumbitButton.setCheckable(True)
        # sumbitButton.toggle()
        # sumbitButton.clicked.connect(lambda:self.whichbtn(sumbitButton))
        # sumbitButton.clicked.connect(self.btnstate)
        
        flo = QFormLayout()
        flo.addRow("NUMBER_OF_CHECKS",e1)
        #TODO: NUMBER_OF_WATS_IN_CHECK need to be arr size of NUMBER_OF_CHECKS
        flo.addRow("NUMBER_OF_WATS_IN_CHECK",e2)
        flo.addRow("PRICES_OF_WATS_IN_CHECK",e3)
        flo.addRow("SERVICE_TAXES",e4)
        flo.addRow("LAST_WATS_OF_SMALL_APARTMENT",e5)
        flo.addRow("WATS_OF_SMALL_APARTMENT_NOW",e6)
        flo.addRow("WATS_OF_BOTH_APARTMENTS",e7)
        flo.addRow(sumbitButton)#,QPushButton("Cancel"))
        
        sumbitButton.clicked.connect(self.button_click)

  
        self.setLayout(flo)

    def button_click(self):
        print("asd")
        # if self.sumbitButton.isChecked():
        #     shost = self.e1.text()
        #     print (shost)
            # inizialize_variables_from_user(self)

def inizialize_variables_from_user(self):
    print(self.e1.text())
class GUI_manager():
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.root = QWidget()
        
        self.root.resize(440,240)
        self.root.setWindowTitle("electric usage calculator")
        
        lineEdit(self.root)
        
        self.root.show()
        sys.exit(self.app.exec_())