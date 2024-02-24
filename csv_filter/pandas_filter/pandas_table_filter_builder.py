
from csv_filter.filter.filter_builder import FilterBuilder
from csv_filter.pandas_filter.pandas_table_filter import PandasTableFilter

from csv_filter.pandas_filter.pandas_single_condition_filter import PandasSingleConditionFilter
from csv_filter.pandas_filter.pandas_two_condition_filter import PandasTwoConditionFilter

from csv_filter.query.condition import Condition
from csv_filter.query.operator import Operator

"""
    Implements the builder interface
"""
class PandasTableFilterBuilder(FilterBuilder):

    def __init__(self) -> None:
        self._conditions = []
        self._operators = []

    def add_operator(self, operator:Operator) -> None:
        self._operators.append(operator)

    def add_condition(self, condition:Condition) -> None:
        self._conditions.append(condition)

    def build(self) -> PandasTableFilter:
        """
            using the conditions and operators build a TableFilter instance
        """
        if len(self._conditions) == 1 and len(self._operators) == 0:
            return PandasSingleConditionFilter(condition=self._conditions[0])

        elif len(self._conditions) == 2 and len(self._operators) == 1:
            return PandasTwoConditionFilter(
                a=self._conditions[0],
                b=self._conditions[1],
                op=self._operators[0]
            )
