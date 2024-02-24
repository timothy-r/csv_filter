import pandas as pd

from csv_filter.query.condition import Condition
from csv_filter.filter.table_filter import TableFilter

"""
    Applies a single condition filter to data frames
    with a single value
"""
class SingleConditionValueFilter(TableFilter):

    def __init__(self, condition:Condition) -> None:
        self._condition = condition

    def apply_filters(self, df:pd.DataFrame) -> pd.DataFrame:

        lhs = self._condition.lhs

        if self._condition.is_equals():
            df = df.loc[df[lhs] == self._condition.rhs]
        elif self._condition.is_greater_than():
            df = df.loc[df[lhs] > self._condition.rhs]
        elif self._condition.is_less_than():
            df = df.loc[df[lhs] < self._condition.rhs]

        return df