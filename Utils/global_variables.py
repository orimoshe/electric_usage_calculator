COUNTRY_TAXES = 0.17    
NUMBER_OF_CHECKS_LAYOUT = 0

def intialize_global_variables(self):
    global NUMBER_OF_WATS_IN_CHECK, NUMBER_OF_CHECKS, WATS_OF_SMALL_APARTMENT_NOW, \
        WATS_OF_BOTH_APARTMENTS, LAST_WATS_OF_SMALL_APARTMENT, PRICES_OF_WATS_IN_CHECK, CHANGE_PRICE_DATE, \
            SERVICE_TAXES, START_DATE, END_DATE, PRECENTAGE_OF_WATS_IN_CHECK
    
    NUMBER_OF_CHECKS = self.number_of_checks

    NUMBER_OF_WATS_IN_CHECK = [0 for check in range(NUMBER_OF_CHECKS)] 
    PRICES_OF_WATS_IN_CHECK = [0 for check in range(NUMBER_OF_CHECKS)]
    CHANGE_PRICE_DATE = [0 for check in range(NUMBER_OF_CHECKS)]
    PRECENTAGE_OF_WATS_IN_CHECK = [0 for check in range(NUMBER_OF_CHECKS)]

    SERVICE_TAXES = float(self.info["service_tax"].text())
    
    for check in range(NUMBER_OF_CHECKS):
        number_of_wats_in_check_name = "number_of_wats_in_check" + "_" + str(check)
        prices_of_wats_in_check_name = "prices_of_wats_in_check" + "_" + str(check)
        change_price_date_name = "change_price_date" + "_" + str(check)
        
        NUMBER_OF_WATS_IN_CHECK[check] = float(self.info[number_of_wats_in_check_name].text())
        PRICES_OF_WATS_IN_CHECK[check] = float(self.info[prices_of_wats_in_check_name].text())
        CHANGE_PRICE_DATE[check] = float(self.info[change_price_date_name].text())
        
    LAST_WATS_OF_SMALL_APARTMENT = float(self.info["last_wats_of_small_apartment"].text())
    WATS_OF_SMALL_APARTMENT_NOW = float(self.info["wats_of_small_apartment_now"].text())
    WATS_OF_BOTH_APARTMENTS = float(self.info["wats_of_both_apartments"].text())
    
    START_DATE = float(self.info["start_date"].text())
    END_DATE = float(self.info["end_date"].text())