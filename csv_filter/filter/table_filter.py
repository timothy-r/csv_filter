import pandas as pd

from abc import ABC, abstractmethod

from csv_filter.query.condition import Condition

"""
    Applies condition filters to pandas data frames
    With one or more conditions
"""
class TableFilter(ABC):

    @abstractmethod
    def apply_filters(self, df:pd.DataFrame) -> pd.DataFrame:
        pass

    def _generate_expression(self,  condition:Condition, df:pd.DataFrame):
        """
            for a single condition generate a filter expression
        """
        if condition.rhs_is_value():
            if condition.is_equals():
                return (df[condition.lhs] == condition.rhs.value)
            elif condition.is_less_than():
                return (df[condition.lhs] < condition.rhs.value)
            elif condition.is_greater_than():
                return (df[condition.lhs] > condition.rhs.value)

        elif condition.rhs_is_list():
            return (df[condition.lhs].isin(condition.rhs.value))