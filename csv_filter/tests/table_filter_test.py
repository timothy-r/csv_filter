import unittest

from csv_filter.parse.table_filter import TableFilter, Condition

class TableFilterTest(unittest.TestCase):

    def test_add_condition(self) -> None:

        filter = TableFilter()

        condition = Condition(lhs='A', comparison='=', rhs='1')

        filter.add_condition(condition=condition)

        self.assertEqual(1, filter.condition_count())
        self.assertEqual(0, filter.operator_count())
        self.assertEqual(condition, filter.condition(0))

    def test_add_operator(self) -> None:

        filter = TableFilter()

        filter.add_operator(operator=TableFilter.OP_AND)

        self.assertEqual(1, filter.operator_count())
        self.assertEqual(0, filter.condition_count())

        op = filter.operator(0)

        self.assertEqual(TableFilter.OP_AND, op)
