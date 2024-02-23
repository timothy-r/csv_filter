from dataclasses import dataclass

from csv_filter.parse.comparison import Comparision

"""
    Class that contains the parts of a condition to filter on
"""
@dataclass(frozen=True)
class Condition:

    lhs: str
    comparison: Comparision
    rhs: str|list

    def __post_init__(self):
        t = type(self.rhs)
        if not t in [str, list]:
            raise TypeError("rhs is an invalid type: {}".format(t))

    def is_equals(self) -> bool:
        return self.comparison == Comparision.EQUALS

    def is_less_than(self) -> bool:
        return self.comparison == Comparision.LESS_THAN

    def is_greater_than(self) -> bool:
        return self.comparison == Comparision.GREATER_THAN