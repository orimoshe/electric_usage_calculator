import Utils.global_variables as g

def get_user_inputs(self):
    g.intialize_global_variables(self)
        
def calculate_precentage_of_wats_in_check(self):
    precentage_of_wats_in_check = [0 for check in range(self.bill_info.NUMBER_OF_CHECKS)]
    
    for check in range(self.bill_info.NUMBER_OF_CHECKS):
        precentage_of_wats_in_check[check] = self.all_checks[check].NUMBER_OF_WATS_IN_CHECK/self.bill_info.WATS_OF_BOTH_APARTMENTS
        self.all_checks[check].PRECENTAGE_OF_WATS_IN_CHECK = precentage_of_wats_in_check[check]
    #TODO: kill this return!
    return precentage_of_wats_in_check

def calculate_wats_of_small_apartment_in_all_checks(self):
    g.WATS_USAGE_OF_SMALL_APARTMENT = self.bill_info.WATS_OF_SMALL_APARTMENT_NOW-self.bill_info.LAST_WATS_OF_SMALL_APARTMENT 
    return (g.WATS_USAGE_OF_SMALL_APARTMENT)
    
def calculate_cost_of_wats_in_check(self, precentage_of_wats_in_check, wats_of_small_apartment_in_all_checks):
    
    for check in range(self.bill_info.NUMBER_OF_CHECKS):
        self.all_checks[check].WATS_OF_SMALL_APARTMENT_IN_CHECK = precentage_of_wats_in_check[check] * wats_of_small_apartment_in_all_checks
        
        self.all_checks[check].COST_OF_WATS_IN_CHECK = precentage_of_wats_in_check[check] * \
            wats_of_small_apartment_in_all_checks * self.all_checks[check].PRICES_OF_WATS_IN_CHECK
        
        self.all_checks[check].COST_OF_WATS_IN_CHECK = round(self.all_checks[check].COST_OF_WATS_IN_CHECK)

def calculate_total_cost_of_wats_in_checks_before_taxes(self):
    total_cost_of_wats_in_checks_before_taxes = 0.0

    for check in range(self.bill_info.NUMBER_OF_CHECKS):
        total_cost_of_wats_in_checks_before_taxes += self.all_checks[check].COST_OF_WATS_IN_CHECK
    
    return total_cost_of_wats_in_checks_before_taxes
    
def calculate_total_cost_of_wats_in_checks_after_taxes(self, total_cost_of_wats_in_checks_before_taxes):
    total_cost_of_wats_in_checks_after_taxes = total_cost_of_wats_in_checks_before_taxes
    total_cost_of_wats_in_checks_after_taxes += self.bill_info.SERVICE_TAXES
    total_cost_of_wats_in_checks_after_taxes += total_cost_of_wats_in_checks_after_taxes * self.bill_info.COUNTRY_TAXES
    g.TOTAL_COST_OF_WATS_IN_CHECKS_AFTER_TAXES = total_cost_of_wats_in_checks_after_taxes
    return total_cost_of_wats_in_checks_after_taxes