
def get_user_inputs():
    global NUMBER_OF_WATS_IN_CHECK, NUMBER_OF_CHECKS, NUMBER_OF_WATS_IN_CHECK, WATS_OF_SMALL_APARTMENT_NOW \
        , WATS_OF_BOTH_APARTMENTS, LAST_WATS_OF_SMALL_APARTMENT
    NUMBER_OF_CHECKS = int(input("enter number of checks: "))

    NUMBER_OF_WATS_IN_CHECK = [0 for check in range(NUMBER_OF_CHECKS)] 
    NUMBER_OF_PRICES_IN_CHECK = [0 for check in range(NUMBER_OF_CHECKS)]
    
    for check in range(NUMBER_OF_CHECKS):
        print("check " + str(check) + ":")
        NUMBER_OF_WATS_IN_CHECK[check] = int(input("enter number of wats in check: "))
        NUMBER_OF_PRICES_IN_CHECK[check] = int(input("enter prices of wats in check: "))
    
    LAST_WATS_OF_SMALL_APARTMENT = int(input("enter last wats of small apartment: "))
    WATS_OF_SMALL_APARTMENT_NOW = int(input("enter wats of small apartment now: "))
    WATS_OF_BOTH_APARTMENTS = int(input("enter wats of both apartment: "))
    
def calculate_precentage_of_wats_in_check():
    precentage_of_wats_in_check = [0 for check in range(NUMBER_OF_CHECKS)]
    
    for check in range(NUMBER_OF_CHECKS):
        precentage_of_wats_in_check[check] = NUMBER_OF_WATS_IN_CHECK[check]/WATS_OF_BOTH_APARTMENTS

    return precentage_of_wats_in_check

def calculate_wats_of_small_apartment_in_all_checks():
    return (WATS_OF_SMALL_APARTMENT_NOW-LAST_WATS_OF_SMALL_APARTMENT)
    
def main():
    get_user_inputs()

    precentage_of_wats_in_check = calculate_precentage_of_wats_in_check()
    wats_of_small_apartment_in_all_checks = calculate_wats_of_small_apartment_in_all_checks()    


if __name__ == "__main__":
    main()
