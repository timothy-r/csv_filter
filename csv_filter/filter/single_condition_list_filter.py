import pandas as pd

from csv_filter.parse.condition import Condition

from csv_filter.filter.table_filter import TableFilter

"""
    Applies a single condition filter to data frames
    With a list of values
"""
class SingleConditionListFilter(TableFilter):

    def __init__(self, condition:Condition) -> None:
        self._condition = condition

    def apply_filters(self, df:pd.DataFrame) -> pd.DataFrame:

        df = df.loc[df[self._condition.lhs].isin(self._condition.rhs)]

        return df