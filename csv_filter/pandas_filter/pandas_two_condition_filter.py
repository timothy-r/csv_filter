import pandas as pd

from csv_filter.query.condition import Condition
from csv_filter.query.operator import Operator
from csv_filter.pandas_filter.pandas_table_filter import PandasTableFilter

"""
    Applies two value condition filters with an operation to pandas data frames
"""
class PandasTwoConditionFilter(PandasTableFilter):

    def __init__(self, a:Condition, op:Operator, b:Condition) -> None:
        self._condition_a = a
        self._operator = op
        self._condition_b = b

    def apply_filters(self, df:pd.DataFrame) -> pd.DataFrame:

        one = self._generate_expression(condition=self._condition_a, df=df)
        two = self._generate_expression(condition=self._condition_b, df=df)

        if self._operator == Operator.AND:
            df = df.loc[one & two]
        elif self._operator == Operator.OR:
            df = df.loc[one | two]

        return df

