from dataclasses import dataclass
@dataclass
class Check:
    NUMBER_OF_CHECKS : int
    NUMBER_OF_WATS_IN_CHECK : float
    WATS_OF_SMALL_APARTMENT_NOW : float
    TOTAL_COST_OF_WATS_IN_CHECKS_AFTER_TAXES : float
    WATS_OF_BOTH_APARTMENTS : float
    LAST_WATS_OF_SMALL_APARTMENT : float
    PRICES_OF_WATS_IN_CHECK : float
    CHANGE_PRICE_DATE : float
    SERVICE_TAXES : float
    START_DATE : float
    END_DATE : float
    PRECENTAGE_OF_WATS_IN_CHECK : float
    COST_OF_WATS_IN_CHECK : float
    WATS_OF_SMALL_APARTMENT_IN_CHECK : float
    
    def create_empty_checks(self) -> list:
        print("create empty check")
        