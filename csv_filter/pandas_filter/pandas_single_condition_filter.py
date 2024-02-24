# import pandas as pd

from csv_filter.query.condition import Condition
from csv_filter.pandas_filter.pandas_table_filter import PandasTableFilter


"""
    Applies a single condition filter to pandas data frames
"""
class PandasSingleConditionFilter(PandasTableFilter):

    def __init__(self, condition:Condition) -> None:
        self._condition = condition

    def apply_filters(self):

        exp = self._generate_expression(condition=self._condition, df=self._df)

        return self._df.loc[exp]
