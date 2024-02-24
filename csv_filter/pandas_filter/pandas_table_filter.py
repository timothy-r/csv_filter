import pandas as pd

from csv_filter.filter.filter import Filter
from csv_filter.query.condition import Condition

"""
    Applies condition filters to pandas data frames
    With one or more conditions
"""
class PandasTableFilter(Filter):

    def set_df(self, df:pd.DataFrame) -> None:
        self._df = df

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