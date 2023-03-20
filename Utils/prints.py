import Utils.global_variables as g
from PyQt5.QtGui import QDoubleValidator, QFont

def base_data(self):
    word = " חשבון החשמל לתקופה שבין"
    word2 = " עד "
    sentence = word + " " + str(g.START_DATE) + word2 + str(g.END_DATE) + ":\n"
        
    word = "בחשבון זה צריכה כוללת "
    sentence += word + str(g.WATS_OF_BOTH_APARTMENTS) + " קוטש" + "\n"
    
    word = "קריאה עדכנית של היחידה "
    sentence += word + str(g.WATS_OF_SMALL_APARTMENT_NOW) + "\n"
    
    word = "קריאה קודמת של היחידה "
    sentence += word + str(g.LAST_WATS_OF_SMALL_APARTMENT) + "\n"
    
    word = "צריכה של היחידה בתקופה זו "
    sentence += word + str(round(g.WATS_USAGE_OF_SMALL_APARTMENT, 1)) + " קוטש" + "\n"

    word = "בחשבון זה חברת חשמל חייבה ב "
    word2 = " תעריפים כדלהלן:"
    sentence += word + str(g.NUMBER_OF_CHECKS) + word2 + "\n"

    word = " עד "
    word2 = " אגורות "
    word3 = " שהם "
    for check in range(g.NUMBER_OF_CHECKS):
        sentence += str(check+1) + "." + word + str(g.CHANGE_PRICE_DATE[check]) + " " + str(round(g.PRICES_OF_WATS_IN_CHECK[check]* 100, 2)) \
            + word2 + str(g.NUMBER_OF_WATS_IN_CHECK[check]) + word3 + str(round(g.PRECENTAGE_OF_WATS_IN_CHECK[check] * 100)) + "%" + "\n"
    
    word = "חישוב תשלום היחידה"
    sentence += word + "\n"
    for check in range(g.NUMBER_OF_CHECKS):
        sentence += str(check+1) + ". " + str(round(g.PRECENTAGE_OF_WATS_IN_CHECK[check] * 100)) + "% " + "מתוך " + \
        str(round(g.WATS_USAGE_OF_SMALL_APARTMENT, 1)) + " קוטש = " + str(round(g.WATS_OF_SMALL_APARTMENT_IN_CHECK[check], 1)) + \
        " קוטש " + "כפול " + str(round(g.PRICES_OF_WATS_IN_CHECK[check]* 100, 2)) + " אגורות " + " = " + \
        str(round(g.COST_OF_WATS_IN_CHECK[check], 2)) + " שח ללא מעמ" + "\n"

    print_on_GUI(self, sentence)

def print_on_GUI(self, word):
    
    self.textLabel.setText(word)
    self.textLabel.setFont(QFont(word, 10))
    self.textLabel.adjustSize() 

    self.textLabel.move(100,100)
    # self.widget.setGeometry(100,100,400,300)


    self.widget.setWindowTitle("Output")
    self.widget.show()
        