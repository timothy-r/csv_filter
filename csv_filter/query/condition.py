from dataclasses import dataclass

from csv_filter.query.comparison import Comparision

from csv_filter.query.rhs import RHS
"""
    Class that contains the parts of a condition to filter on
"""
@dataclass(frozen=True)
class Condition:

    lhs: str
    comparison: Comparision
    rhs: RHS

    def is_equals(self) -> bool:
        return self.comparison == Comparision.EQUALS

    def is_less_than(self) -> bool:
        return self.comparison == Comparision.LESS_THAN

    def is_greater_than(self) -> bool:
        return self.comparison == Comparision.GREATER_THAN

    def rhs_is_value(self) -> bool:
        return self.rhs.is_value()

    def rhs_is_list(self) -> bool:
        return self.rhs.is_list()
