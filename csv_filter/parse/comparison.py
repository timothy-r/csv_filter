from enum import Enum


class Comparision(Enum):

    EQUALS = '='
    GREATER_THAN = '>'
    LESS_THAN = '<'

    @staticmethod
    def from_str(value:str) -> "Comparision":
        if value == Comparision.EQUALS.value:
            return Comparision.EQUALS
        elif value == Comparision.LESS_THAN.value:
            return Comparision.LESS_THAN
        elif value == Comparision.GREATER_THAN.value:
            return Comparision.GREATER_THAN
        else:
            raise ValueError("Comparison {} is invalid".format(value))

    @staticmethod
    def valid_comparisons() -> list:
        return [Comparision.LESS_THAN.value, Comparision.EQUALS.value, Comparision.GREATER_THAN.value]

