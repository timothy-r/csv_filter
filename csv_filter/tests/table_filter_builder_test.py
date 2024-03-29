import unittest

from csv_filter.pandas_filter.pandas_table_filter_builder import PandasTableFilterBuilder
from csv_filter.pandas_filter.pandas_table_filter import PandasTableFilter

from csv_filter.pandas_filter.pandas_single_condition_filter import PandasSingleConditionFilter
from csv_filter.pandas_filter.pandas_two_condition_filter import PandasTwoConditionFilter

from csv_filter.query.operator import Operator
from csv_filter.query.condition import Condition
from csv_filter.query.comparison import Comparision

class TableFilterBuilderTest(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        self._builder = PandasTableFilterBuilder()

    def test_build_single_condition_value_filter(self) -> None:

        condition = Condition('A', Comparision.EQUALS, '5')
        self._builder.add_condition(condition=condition)

        table_filter = self._builder.build()
        self.assertIsInstance(table_filter, PandasSingleConditionFilter)

    def test_build_single_condition_list_filter(self) -> None:

        condition = Condition('A', Comparision.EQUALS, ['5', '8'])
        self._builder.add_condition(condition=condition)

        table_filter = self._builder.build()
        self.assertIsInstance(table_filter, PandasSingleConditionFilter)

    def test_build_two_condition_filter(self) -> None:
        condition_a = Condition('A', Comparision.EQUALS, '5')
        condition_b = Condition('B', Comparision.GREATER_THAN, '100')

        self._builder.add_condition(condition=condition_a)
        self._builder.add_operator(Operator.AND)
        self._builder.add_condition(condition=condition_b)

        table_filter = self._builder.build()
        self.assertIsInstance(table_filter, PandasTwoConditionFilter)

