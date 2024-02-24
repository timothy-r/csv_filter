import pandas as pd

from csv_filter.query.condition import Condition
from csv_filter.filter.table_filter import TableFilter

"""
    Applies a single condition filter to data frames
    with a single value
"""
class SingleConditionFilter(TableFilter):

    def __init__(self, condition:Condition) -> None:
        self._condition = condition

    def apply_filters(self, df:pd.DataFrame) -> pd.DataFrame:

        exp = self._generate_expression(condition=self._condition, df=df)

        return df.loc[exp]
