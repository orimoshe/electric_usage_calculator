from utils import *

def main():
    get_user_inputs()
    precentage_of_wats_in_check = calculate_precentage_of_wats_in_check()    
    wats_of_small_apartment_in_all_checks = calculate_wats_of_small_apartment_in_all_checks()   
    cost_of_wats_in_check = calculate_cost_of_wats_in_check(precentage_of_wats_in_check, wats_of_small_apartment_in_all_checks)
    total_cost_of_wats_in_checks_before_taxes = calculate_total_cost_of_wats_in_checks_before_taxes(cost_of_wats_in_check)

    total_cost_of_wats_in_checks_after_taxes = calculate_total_cost_of_wats_in_checks_after_taxes(total_cost_of_wats_in_checks_before_taxes)
    print("total pay of small apartment " + str(total_cost_of_wats_in_checks_after_taxes))
if __name__ == "__main__":
    main()
