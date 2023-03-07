COUNTRY_TAXES = 0.17    

def intialize_global_variables():
    global NUMBER_OF_WATS_IN_CHECK, NUMBER_OF_CHECKS, WATS_OF_SMALL_APARTMENT_NOW \
        , WATS_OF_BOTH_APARTMENTS, LAST_WATS_OF_SMALL_APARTMENT, PRICES_OF_WATS_IN_CHECK, SERVICE_TAXES
    
    NUMBER_OF_CHECKS = int(input("enter number of checks: "))
    
    NUMBER_OF_WATS_IN_CHECK = [0 for check in range(NUMBER_OF_CHECKS)] 
    PRICES_OF_WATS_IN_CHECK = [0 for check in range(NUMBER_OF_CHECKS)]
    
    SERVICE_TAXES = float(input("enter service taxes: "))
    
    for check in range(NUMBER_OF_CHECKS):
        print("check " + str(check) + ":")
        NUMBER_OF_WATS_IN_CHECK[check] = float(input("enter number of wats in check: "))
        PRICES_OF_WATS_IN_CHECK[check] = float(input("enter the price of wats in check: "))
        
    LAST_WATS_OF_SMALL_APARTMENT = float(input("enter last wats of small apartment: "))
    WATS_OF_SMALL_APARTMENT_NOW = float(input("enter wats of small apartment now: "))
    WATS_OF_BOTH_APARTMENTS = float(input("enter wats of both apartment: "))