from dataclasses import dataclass

"""
    Class that contains the parts of a condition to filter on
"""
@dataclass(frozen=True)
class Condition:

    lhs: str
    comparison: str
    rhs: str|list

    EQUALS = '='
    GREATER_THAN = '>'
    LESS_THAN = '<'

    def __post_init__(self):
        if self.comparison not in Condition.valid_comparisons():
            raise ValueError("Comparison {} is invalid".format(self.comparison))

        t = type(self.rhs)
        if not t in [str, list]:
            raise TypeError("rhs is an invalid type: {}".format(t))

    @staticmethod
    def valid_comparisons() -> list:
        return [Condition.LESS_THAN, Condition.EQUALS, Condition.GREATER_THAN]
