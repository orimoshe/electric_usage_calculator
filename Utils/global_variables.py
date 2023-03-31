from Utils.Bill import *

COUNTRY_TAXES = 0.17
NUMBER_OF_CHECKS_LAYOUT = 0
INPUT_NAMES = ["תאריך התחלת החשבון", "תאריך סוף החשבון","תאריך שינוי המחיר", "כמות הוואט בחשבון",\
            "מחיר הוואט בחשבון", "צריכת הוואט בדירה הקטנה עכשיו", "צריכת הוואט בשתי הדירות", \
                            "קריאת הוואט הקודמת בדירה הקטנה", "תשלום קבוע"]

def intialize_global_variables(self):
    global NUMBER_OF_WATS_IN_CHECK, WATS_OF_SMALL_APARTMENT_NOW, TOTAL_COST_OF_WATS_IN_CHECKS_AFTER_TAXES, \
        WATS_OF_BOTH_APARTMENTS, LAST_WATS_OF_SMALL_APARTMENT, PRICES_OF_WATS_IN_CHECK, CHANGE_PRICE_DATE, \
        SERVICE_TAXES, START_DATE, END_DATE, PRECENTAGE_OF_WATS_IN_CHECK, COST_OF_WATS_IN_CHECK, WATS_OF_SMALL_APARTMENT_IN_CHECK
    
    # bill_info.NUMBER_OF_CHECKS = self.number_of_checks
    # NUMBER_OF_CHECKS = self.number_of_checks

    COST_OF_WATS_IN_CHECK = [0 for check in range(self.bill_info.NUMBER_OF_CHECKS)]
    WATS_OF_SMALL_APARTMENT_IN_CHECK = [0 for check in range(self.bill_info.NUMBER_OF_CHECKS)]
    NUMBER_OF_WATS_IN_CHECK = [0 for check in range(self.bill_info.NUMBER_OF_CHECKS)] 
    PRICES_OF_WATS_IN_CHECK = [0 for check in range(self.bill_info.NUMBER_OF_CHECKS)]
    CHANGE_PRICE_DATE = [0 for check in range(self.bill_info.NUMBER_OF_CHECKS)]
    PRECENTAGE_OF_WATS_IN_CHECK = [0 for check in range(self.bill_info.NUMBER_OF_CHECKS)]

    SERVICE_TAXES = float(self.info["תשלום קבוע"].text())
    
    for check in range(self.bill_info.NUMBER_OF_CHECKS):
        number_of_wats_in_check_name = "כמות הוואט בחשבון" + " " + str(check+1)
        prices_of_wats_in_check_name = "מחיר הוואט בחשבון" + " " + str(check+1)
        change_price_date_name = "תאריך שינוי המחיר" + " " + str(check+1)
        
        NUMBER_OF_WATS_IN_CHECK[check] = float(self.info[number_of_wats_in_check_name].text())
        PRICES_OF_WATS_IN_CHECK[check] = float(self.info[prices_of_wats_in_check_name].text())
        CHANGE_PRICE_DATE[check] = float(self.info[change_price_date_name].text())
        
    LAST_WATS_OF_SMALL_APARTMENT = float(self.info["קריאת הוואט הקודמת בדירה הקטנה"].text())
    WATS_OF_SMALL_APARTMENT_NOW = float(self.info["צריכת הוואט בדירה הקטנה עכשיו"].text())
    WATS_OF_BOTH_APARTMENTS = float(self.info["צריכת הוואט בשתי הדירות"].text())
    
    START_DATE = float(self.info["תאריך התחלת החשבון"].text())
    END_DATE = float(self.info["תאריך סוף החשבון"].text())