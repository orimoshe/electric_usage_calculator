from Utils.Bill import *
from Utils.Check import *

def create_checks(self, number_of_wats_in_check_name, prices_of_wats_in_check_name, change_price_date_name):
    self.all_checks = []
    for check in range(self.bill_info.NUMBER_OF_CHECKS):
        self.all_checks.append(Check(
                                NUMBER_OF_WATS_IN_CHECK = float(self.info[number_of_wats_in_check_name[check]].text()),
                                
                                PRICES_OF_WATS_IN_CHECK = float(self.info[prices_of_wats_in_check_name[check]].text()),
                                CHANGE_PRICE_DATE = float(self.info[change_price_date_name[check]].text())
            ))

def intialize_global_variables(self):
    global WATS_OF_SMALL_APARTMENT_NOW, TOTAL_COST_OF_WATS_IN_CHECKS_AFTER_TAXES, \
        WATS_OF_BOTH_APARTMENTS, LAST_WATS_OF_SMALL_APARTMENT, \
        SERVICE_TAXES, START_DATE, END_DATE
    
    #TODOO: add this three into Check struct
    # COST_OF_WATS_IN_CHECK = [0 for check in range(self.bill_info.NUMBER_OF_CHECKS)]
    # WATS_OF_SMALL_APARTMENT_IN_CHECK = [0 for check in range(self.bill_info.NUMBER_OF_CHECKS)]
    # PRECENTAGE_OF_WATS_IN_CHECK = [0 for check in range(self.bill_info.NUMBER_OF_CHECKS)]

    SERVICE_TAXES = float(self.info["תשלום קבוע"].text())
    
    number_of_wats_in_check_name = []
    prices_of_wats_in_check_name = []
    change_price_date_name = []
    for check in range(self.bill_info.NUMBER_OF_CHECKS):
        number_of_wats_in_check_name.append("כמות הוואט בחשבון" + " " + str(check+1))
        prices_of_wats_in_check_name.append("מחיר הוואט בחשבון" + " " + str(check+1))
        change_price_date_name.append("תאריך שינוי המחיר" + " " + str(check+1))
    
    create_checks(self, number_of_wats_in_check_name, prices_of_wats_in_check_name, change_price_date_name)
    
    LAST_WATS_OF_SMALL_APARTMENT = float(self.info["קריאת הוואט הקודמת בדירה הקטנה"].text())
    WATS_OF_SMALL_APARTMENT_NOW = float(self.info["צריכת הוואט בדירה הקטנה עכשיו"].text())
    WATS_OF_BOTH_APARTMENTS = float(self.info["צריכת הוואט בשתי הדירות"].text())
    
    START_DATE = float(self.info["תאריך התחלת החשבון"].text())
    END_DATE = float(self.info["תאריך סוף החשבון"].text())