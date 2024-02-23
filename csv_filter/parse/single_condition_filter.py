import pandas as pd

from csv_filter.parse.condition import Condition

"""
    Applies a single condition filter to data frames
"""
class SingleConditionFilter():

    def __init__(self, condition:Condition) -> None:
        self._condition = condition

    def apply_filters(self, df:pd.DataFrame) -> pd.DataFrame:

        lhs = self._condition.lhs

        if type(self._condition.rhs) == str:
            if self._condition.is_equals():
                df = df.loc[df[lhs] == self._condition.rhs]
            elif self._condition.is_greater_than():
                df = df.loc[df[lhs] > self._condition.rhs]
            elif self._condition.is_less_than():
                df = df.loc[df[lhs] < self._condition.rhs]

        elif type(self._condition.rhs) == list:
            if self._condition.is_equals():
                df = df.loc[df[lhs].isin(self._condition.rhs)]
            else:
                raise TypeError
        else:
            raise TypeError

        return df