from dataclasses import dataclass, field
from typing import List

#TODO: add "kw_only=True" to dataclass as argument
def generate_input_names() -> list:
    return ["תאריך התחלת החשבון", "תאריך סוף החשבון","תאריך שינוי המחיר", "כמות הוואט בחשבון",\
                                "מחיר הוואט בחשבון", "צריכת הוואט בדירה הקטנה עכשיו", "צריכת הוואט בשתי הדירות", \
                                "קריאת הוואט הקודמת בדירה הקטנה", "תשלום קבוע"]
@dataclass(frozen=True)
class Bill:
    NUMBER_OF_CHECKS : int

    COUNTRY_TAXES : float = 0.17
    NUMBER_OF_CHECKS_LAYOUT : int = 0
    INPUT_NAMES : list = field(default_factory=generate_input_names)