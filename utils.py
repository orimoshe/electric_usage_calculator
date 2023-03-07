COUNTRY_TAXES = 0.17

def get_user_inputs():
    global NUMBER_OF_WATS_IN_CHECK, NUMBER_OF_CHECKS, NUMBER_OF_WATS_IN_CHECK, WATS_OF_SMALL_APARTMENT_NOW \
        , WATS_OF_BOTH_APARTMENTS, LAST_WATS_OF_SMALL_APARTMENT, PRICES_OF_WATS_IN_CHECK, SERVICE_TAXES
    SERVICE_TAXES = float(input("enter service taxes: "))
    NUMBER_OF_CHECKS = int(input("enter number of checks: "))

    NUMBER_OF_WATS_IN_CHECK = [0 for check in range(NUMBER_OF_CHECKS)] 
    PRICES_OF_WATS_IN_CHECK = [0 for check in range(NUMBER_OF_CHECKS)]
    
    for check in range(NUMBER_OF_CHECKS):
        print("check " + str(check) + ":")
        NUMBER_OF_WATS_IN_CHECK[check] = float(input("enter number of wats in check: "))
        PRICES_OF_WATS_IN_CHECK[check] = float(input("enter the price of wats in check: "))
        
    LAST_WATS_OF_SMALL_APARTMENT = float(input("enter last wats of small apartment: "))
    WATS_OF_SMALL_APARTMENT_NOW = float(input("enter wats of small apartment now: "))
    WATS_OF_BOTH_APARTMENTS = float(input("enter wats of both apartment: "))
    
def calculate_precentage_of_wats_in_check():
    precentage_of_wats_in_check = [0 for check in range(NUMBER_OF_CHECKS)]
    
    for check in range(NUMBER_OF_CHECKS):
        precentage_of_wats_in_check[check] = NUMBER_OF_WATS_IN_CHECK[check]/WATS_OF_BOTH_APARTMENTS

    return precentage_of_wats_in_check

def calculate_wats_of_small_apartment_in_all_checks():
    return (WATS_OF_SMALL_APARTMENT_NOW-LAST_WATS_OF_SMALL_APARTMENT)
    
def calculate_cost_of_wats_in_check(precentage_of_wats_in_check, wats_of_small_apartment_in_all_checks):
    cost_of_wats_in_check = [0 for check in range(NUMBER_OF_CHECKS)]

    for check in range(NUMBER_OF_CHECKS):
        cost_of_wats_in_check[check] = precentage_of_wats_in_check[check] * \
            wats_of_small_apartment_in_all_checks * PRICES_OF_WATS_IN_CHECK[check]
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
    total_cost_of_wats_in_checks_after_taxes = total_cost_of_wats_in_checks_after_taxes + SERVICE_TAXES
    total_cost_of_wats_in_checks_after_taxes = total_cost_of_wats_in_checks_after_taxes + \
        (total_cost_of_wats_in_checks_after_taxes * COUNTRY_TAXES)
    return total_cost_of_wats_in_checks_after_taxes