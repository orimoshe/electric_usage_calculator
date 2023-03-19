import Utils.global_variables as g
def base_data(self):
    word = u"חשבון החשמל לתקופה שבין "
    word2 = u"עד "
    word = word[::-1]
    word2 = word2[::-1]
    print(str(g.END_DATE) + word2 + " " + str(g.START_DATE) + word)
    
    
    word = u"בחשבון זה צריכה כוללת "
    word = word[::-1]
    print(str(g.WATS_OF_BOTH_APARTMENTS) + word)
    
    word = u"קריאה עדכנית של היחידה "
    word = word[::-1]
    print(str(g.WATS_OF_SMALL_APARTMENT_NOW) + word)
    
    word = u"קריאה קודמת של היחידה "
    word = word[::-1]
    print(str(g.LAST_WATS_OF_SMALL_APARTMENT) + word)
    
    word = u"צריכה של היחידה בתקופה זו "
    word = word[::-1]
    print(str(g.WATS_USAGE_OF_SMALL_APARTMENT) + word)

    word = u"בחשבון זה חברת חשמל חייבה ב "
    word2 = u" תעריפים כדלהלן:"
    word = word[::-1]
    word2 = word2[::-1]
    print(word2 + str(g.NUMBER_OF_CHECKS) + word)

    word = u" עד "
    word2 = u" אגורות "
    word3 = u" שהם "
    word = word[::-1]
    word2 = word2[::-1]
    word3 = word3[::-1]
    for check in range(g.NUMBER_OF_CHECKS):
        print(str(check+1) + "." + word + str(g.CHANGE_PRICE_DATE[check]) + " " + str(round(g.PRICES_OF_WATS_IN_CHECK[check]* 100, 2)) \
            + word2 + str(g.NUMBER_OF_WATS_IN_CHECK[check]) + word3 + str(round(g.PRECENTAGE_OF_WATS_IN_CHECK[check] * 100)) + "%")
    
    print_on_GUI(self)

def print_on_GUI(self):
    word = u" עד "
    
    self.textLabel.setText(word)
    self.textLabel.move(110,85)
    # self.widget.setGeometry(50,50,320,200)
    self.widget.setWindowTitle("Output")
    self.widget.show()
        