import Utils.global_variables as g

def get_user_inputs(self):
    g.intialize_global_variables(self)
        
def calculate_precentage_of_wats_in_check(self):
    precentage_of_wats_in_check = [0 for check in range(self.bill_info.NUMBER_OF_CHECKS)]
    
    for check in range(self.bill_info.NUMBER_OF_CHECKS):
        precentage_of_wats_in_check[check] = self.all_checks[check].NUMBER_OF_WATS_IN_CHECK/g.WATS_OF_BOTH_APARTMENTS
        g.PRECENTAGE_OF_WATS_IN_CHECK[check] = precentage_of_wats_in_check[check]
    return precentage_of_wats_in_check

def calculate_wats_of_small_apartment_in_all_checks():
    g.WATS_USAGE_OF_SMALL_APARTMENT = g.WATS_OF_SMALL_APARTMENT_NOW-g.LAST_WATS_OF_SMALL_APARTMENT 
    return (g.WATS_USAGE_OF_SMALL_APARTMENT)
    
def calculate_cost_of_wats_in_check(self, precentage_of_wats_in_check, wats_of_small_apartment_in_all_checks):
    cost_of_wats_in_check = [0 for check in range(self.bill_info.NUMBER_OF_CHECKS)]

    
    for check in range(self.bill_info.NUMBER_OF_CHECKS):
        #TODO: put and replace using this global variable in the calculation 
        g.WATS_OF_SMALL_APARTMENT_IN_CHECK[check] = precentage_of_wats_in_check[check] * wats_of_small_apartment_in_all_checks
        
        cost_of_wats_in_check[check] = precentage_of_wats_in_check[check] * \
            wats_of_small_apartment_in_all_checks * self.all_checks[check].PRICES_OF_WATS_IN_CHECK
        cost_of_wats_in_check[check] = round(cost_of_wats_in_check[check])
    g.COST_OF_WATS_IN_CHECK = cost_of_wats_in_check
    return cost_of_wats_in_check

def calculate_total_cost_of_wats_in_checks_before_taxes(cost_of_wats_in_check):
    total_cost_of_wats_in_checks_before_taxes = 0.0
    for cost_of_wats_in_specific_check in cost_of_wats_in_check:
        total_cost_of_wats_in_checks_before_taxes += cost_of_wats_in_specific_check
    return total_cost_of_wats_in_checks_before_taxes
    
#TODO: use global total_cost_of_wats_in_checks_after_taxes
def calculate_total_cost_of_wats_in_checks_after_taxes(self, total_cost_of_wats_in_checks_before_taxes):
    total_cost_of_wats_in_checks_after_taxes = total_cost_of_wats_in_checks_before_taxes
    total_cost_of_wats_in_checks_after_taxes += g.SERVICE_TAXES
    total_cost_of_wats_in_checks_after_taxes += total_cost_of_wats_in_checks_after_taxes * self.bill_info.COUNTRY_TAXES
    g.TOTAL_COST_OF_WATS_IN_CHECKS_AFTER_TAXES = total_cost_of_wats_in_checks_after_taxes
    return total_cost_of_wats_in_checks_after_taxes