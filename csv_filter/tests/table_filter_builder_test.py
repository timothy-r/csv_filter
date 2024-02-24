import unittest

from csv_filter.filter.table_filter_builder import TableFilterBuilder
from csv_filter.filter.table_filter import TableFilter
from csv_filter.filter.single_condition_list_filter import SingleConditionListFilter
from csv_filter.filter.single_condition_value_filter import SingleConditionValueFilter

from csv_filter.query.operator import Operator
from csv_filter.query.condition import Condition
from csv_filter.query.comparison import Comparision

class TableFilterBuilderTest(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        self._builder = TableFilterBuilder()

    def test_build_single_condition_value_filter(self) -> None:

        condition = Condition('A', Comparision.EQUALS, '5')
        self._builder.add_condition(condition=condition)

        table_filter = self._builder.build()
        self.assertIsInstance(table_filter, SingleConditionValueFilter)

    def test_build_single_condition_list_filter(self) -> None:

        condition = Condition('A', Comparision.EQUALS, ['5', '8'])
        self._builder.add_condition(condition=condition)

        table_filter = self._builder.build()
        self.assertIsInstance(table_filter, SingleConditionListFilter)

