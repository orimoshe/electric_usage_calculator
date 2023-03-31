from dataclasses import dataclass

#TODO: add "kw_only=True" to dataclass as argument
@dataclass(frozen=True)
class Bill:
    NUMBER_OF_CHECKS : int