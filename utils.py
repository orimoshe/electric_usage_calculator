import global_variables as g

def get_user_inputs():
    g.intialize_global_variables()
        
def calculate_precentage_of_wats_in_check():
    precentage_of_wats_in_check = [0 for check in range(g.NUMBER_OF_CHECKS)]
    
    for check in range(g.NUMBER_OF_CHECKS):
        precentage_of_wats_in_check[check] = g.NUMBER_OF_WATS_IN_CHECK[check]/g.WATS_OF_BOTH_APARTMENTS

    return precentage_of_wats_in_check

def calculate_wats_of_small_apartment_in_all_checks():
    return (g.WATS_OF_SMALL_APARTMENT_NOW-g.LAST_WATS_OF_SMALL_APARTMENT)
    
def calculate_cost_of_wats_in_check(precentage_of_wats_in_check, wats_of_small_apartment_in_all_checks):
    cost_of_wats_in_check = [0 for check in range(g.NUMBER_OF_CHECKS)]

    for check in range(g.NUMBER_OF_CHECKS):
        cost_of_wats_in_check[check] = precentage_of_wats_in_check[check] * \
            wats_of_small_apartment_in_all_checks * g.PRICES_OF_WATS_IN_CHECK[check]
        cost_of_wats_in_check[check] = round(cost_of_wats_in_check[check])
    return cost_of_wats_in_check

def calculate_total_cost_of_wats_in_checks_before_taxes(cost_of_wats_in_check):
    total_cost_of_wats_in_checks_before_taxes = 0.0
    for cost_of_wats_in_specific_check in cost_of_wats_in_check:
        total_cost_of_wats_in_checks_before_taxes = total_cost_of_wats_in_checks_before_taxes + \
            cost_of_wats_in_specific_check
    return total_cost_of_wats_in_checks_before_taxes
    
def calculate_total_cost_of_wats_in_checks_after_taxes(total_cost_of_wats_in_checks_before_taxes):
    total_cost_of_wats_in_checks_after_taxes = total_cost_of_wats_in_checks_before_taxes
    total_cost_of_wats_in_checks_after_taxes = total_cost_of_wats_in_checks_after_taxes + g.SERVICE_TAXES
    total_cost_of_wats_in_checks_after_taxes = total_cost_of_wats_in_checks_after_taxes + \
        (total_cost_of_wats_in_checks_after_taxes * g.COUNTRY_TAXES)
    return total_cost_of_wats_in_checks_after_taxes