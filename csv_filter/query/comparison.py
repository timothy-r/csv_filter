from enum import Enum

"""
    Encapsulates valid comparisons
"""

class Comparision(Enum):

    EQUALS = '='
    GREATER_THAN = '>'
    LESS_THAN = '<'

    @staticmethod
    def valid_comparisons() -> list:
        return [Comparision.LESS_THAN.value, Comparision.EQUALS.value, Comparision.GREATER_THAN.value]

