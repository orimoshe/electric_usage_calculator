import Utils.global_variables as g

#TODOOO: use f"string" instead of +
def base_data(self):
    word = " חשבון החשמל לתקופה שבין"
    word2 = " עד "
    sentence = word + " " + str(self.bill_info.START_DATE) + word2 + str(self.bill_info.END_DATE) + ":\n\n"
        
    word = "בחשבון זה צריכה כוללת "
    sentence += word + str(self.bill_info.WATS_OF_BOTH_APARTMENTS) + " קוטש" + "\n\n"
    
    word = "קריאה עדכנית של היחידה "
    sentence += word + str(self.bill_info.WATS_OF_SMALL_APARTMENT_NOW) + "\n"
    
    word = "קריאה קודמת של היחידה "
    sentence += word + str(self.bill_info.LAST_WATS_OF_SMALL_APARTMENT) + "\n\n"
    
    word = "צריכה של היחידה בתקופה זו "
    sentence += word + str(round(g.WATS_USAGE_OF_SMALL_APARTMENT, 1)) + " קוטש" + "\n\n"

    word = "בחשבון זה חברת חשמל חייבה ב "
    word2 = " תעריפים כדלהלן:"
    sentence += word + str(self.bill_info.NUMBER_OF_CHECKS) + word2 + "\n"

    word = " עד "
    word2 = " אגורות "
    word3 = " שהם "
    for check in range(self.bill_info.NUMBER_OF_CHECKS):
        sentence += str(check+1) + "." + word + str(self.all_checks[check].CHANGE_PRICE_DATE) + " " + str(round(self.all_checks[check].PRICES_OF_WATS_IN_CHECK* 100, 2)) \
            + word2 + str(self.all_checks[check].NUMBER_OF_WATS_IN_CHECK) + word3 + str(round(self.all_checks[check].PRECENTAGE_OF_WATS_IN_CHECK * 100)) + "%" + "\n"
    
    word = "\n" + "חישוב תשלום היחידה"
    sentence += word + "\n"
    for check in range(self.bill_info.NUMBER_OF_CHECKS):
        sentence += str(check+1) + ". " + str(round(self.all_checks[check].PRECENTAGE_OF_WATS_IN_CHECK * 100)) + "% " + "מתוך " + \
        str(round(g.WATS_USAGE_OF_SMALL_APARTMENT, 1)) + " קוטש = " + str(round(self.all_checks[check].WATS_OF_SMALL_APARTMENT_IN_CHECK, 1)) + \
        " קוטש " + "כפול " + str(round(self.all_checks[check].PRICES_OF_WATS_IN_CHECK* 100, 2)) + " אגורות " + " = " + \
        str(round(self.all_checks[check].COST_OF_WATS_IN_CHECK, 2)) + " שח ללא מעמ" + "\n"

    word = "\n" + "הוספת מעמ"
    sentence += word + "\n"
    total_cost_in_check = 0.0
    for check in range(self.bill_info.NUMBER_OF_CHECKS):
        total_cost_in_check += self.all_checks[check].COST_OF_WATS_IN_CHECK
        sentence += str(round(self.all_checks[check].COST_OF_WATS_IN_CHECK, 2))
        if(check+1 != self.bill_info.NUMBER_OF_CHECKS):
            sentence += " + "
    
    sentence += " = " + str(total_cost_in_check) + " + " + str(self.bill_info.SERVICE_TAXES) + " שח תשלום קבוע " 
    total_cost_in_check += self.bill_info.SERVICE_TAXES
    sentence += str(total_cost_in_check) + " + 17% = " + str(g.TOTAL_COST_OF_WATS_IN_CHECKS_AFTER_TAXES) + "שח" + "\n"
    sentence += " סהכ חשבון היחידה לתקופה זו " + str(g.TOTAL_COST_OF_WATS_IN_CHECKS_AFTER_TAXES) + "שח"
        
    print_on_GUI(self, sentence)

def print_on_GUI(self, word):
    
    self.textLabel.setText(word)
    self.textLabel.adjustSize() 

    self.textLabel.move(100,100)

    self.widget.setWindowTitle("Output")
    self.widget.show()