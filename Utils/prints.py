import Utils.global_variables as g

#TODOOO: use f"string" instead of +
def base_data(self):
    word = " חשבון החשמל לתקופה שבין"
    word2 = " עד "
    sentence = word + " " + str(g.START_DATE) + word2 + str(g.END_DATE) + ":\n\n"
        
    word = "בחשבון זה צריכה כוללת "
    sentence += word + str(g.WATS_OF_BOTH_APARTMENTS) + " קוטש" + "\n\n"
    
    word = "קריאה עדכנית של היחידה "
    sentence += word + str(g.WATS_OF_SMALL_APARTMENT_NOW) + "\n"
    
    word = "קריאה קודמת של היחידה "
    sentence += word + str(g.LAST_WATS_OF_SMALL_APARTMENT) + "\n\n"
    
    word = "צריכה של היחידה בתקופה זו "
    sentence += word + str(round(g.WATS_USAGE_OF_SMALL_APARTMENT, 1)) + " קוטש" + "\n\n"

    word = "בחשבון זה חברת חשמל חייבה ב "
    word2 = " תעריפים כדלהלן:"
    sentence += word + str(self.bill_info.NUMBER_OF_CHECKS) + word2 + "\n"

    word = " עד "
    word2 = " אגורות "
    word3 = " שהם "
    for check in range(self.bill_info.NUMBER_OF_CHECKS):
        sentence += str(check+1) + "." + word + str(g.CHANGE_PRICE_DATE[check]) + " " + str(round(g.PRICES_OF_WATS_IN_CHECK[check]* 100, 2)) \
            + word2 + str(g.NUMBER_OF_WATS_IN_CHECK[check]) + word3 + str(round(g.PRECENTAGE_OF_WATS_IN_CHECK[check] * 100)) + "%" + "\n"
    
    word = "\n" + "חישוב תשלום היחידה"
    sentence += word + "\n"
    for check in range(self.bill_info.NUMBER_OF_CHECKS):
        sentence += str(check+1) + ". " + str(round(g.PRECENTAGE_OF_WATS_IN_CHECK[check] * 100)) + "% " + "מתוך " + \
        str(round(g.WATS_USAGE_OF_SMALL_APARTMENT, 1)) + " קוטש = " + str(round(g.WATS_OF_SMALL_APARTMENT_IN_CHECK[check], 1)) + \
        " קוטש " + "כפול " + str(round(g.PRICES_OF_WATS_IN_CHECK[check]* 100, 2)) + " אגורות " + " = " + \
        str(round(g.COST_OF_WATS_IN_CHECK[check], 2)) + " שח ללא מעמ" + "\n"

    word = "\n" + "הוספת מעמ"
    sentence += word + "\n"
    total_cost_in_check = 0.0
    for check in range(self.bill_info.NUMBER_OF_CHECKS):
        total_cost_in_check += g.COST_OF_WATS_IN_CHECK[check]
        sentence += str(round(g.COST_OF_WATS_IN_CHECK[check], 2))
        if(check+1 != self.bill_info.NUMBER_OF_CHECKS):
            sentence += " + "
    
    sentence += " = " + str(total_cost_in_check) + " + " + str(g.SERVICE_TAXES) + " שח תשלום קבוע " 
    total_cost_in_check += g.SERVICE_TAXES
    sentence += str(total_cost_in_check) + " + 17% = " + str(g.TOTAL_COST_OF_WATS_IN_CHECKS_AFTER_TAXES) + "שח" + "\n"
    sentence += " סהכ חשבון היחידה לתקופה זו " + str(g.TOTAL_COST_OF_WATS_IN_CHECKS_AFTER_TAXES) + "שח"
        
    print_on_GUI(self, sentence)

def print_on_GUI(self, word):
    
    self.textLabel.setText(word)
    self.textLabel.adjustSize() 

    self.textLabel.move(100,100)

    self.widget.setWindowTitle("Output")
    self.widget.show()