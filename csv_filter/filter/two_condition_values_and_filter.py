import pandas as pd

from csv_filter.parse.condition import Condition
from csv_filter.parse.table_filter import TableFilter

"""
    Applies two value condition filters with an and operations to data frames
"""
class TwoConditionValuesAndFilter(TableFilter):

    def __init__(self, a:Condition, b:Condition) -> None:
        self._condition_a = a
        self._condition_b = b

    def apply_filters(self, df:pd.DataFrame) -> pd.DataFrame:
        # apply comparisons as well
        if self._condition_a.is_equals() and self._condition_b.is_equals():
            df = df.loc[
                (df[self._condition_a.lhs] == self._condition_a.rhs)
                &
                (df[self._condition_b.lhs] == self._condition_b.rhs)
                ]
        elif self._condition_a.is_equals() and self._condition_b.is_less_than():
            df = df.loc[
                (df[self._condition_a.lhs] == self._condition_a.rhs)
                &
                (df[self._condition_b.lhs] < self._condition_b.rhs)
                ]

        # else:
            # raise TypeError

        return df