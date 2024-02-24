import pandas as pd

from csv_filter.query.condition import Condition
from csv_filter.parse.table_filter import TableFilter

"""
    Applies two value condition filters with an and operations to data frames
"""
class TwoConditionValuesAndFilter(TableFilter):

    def __init__(self, a:Condition, b:Condition) -> None:
        self._condition_a = a
        self._condition_b = b

    def apply_filters(self, df:pd.DataFrame) -> pd.DataFrame:

        one = self._generate_expression(condition=self._condition_a, df=df)
        two = self._generate_expression(condition=self._condition_b, df=df)

        df = df.loc[one & two]

        return df

