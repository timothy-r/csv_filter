import unittest

from csv_filter.parse.condition import Condition
from csv_filter.parse.comparison import Comparision

class ConditionTest(unittest.TestCase):

    def test_is_equals(self) -> None:

        cond = Condition('A', Comparision.EQUALS, '4')
        self.assertTrue(cond.is_equals())

        cond_b = Condition('X', Comparision.LESS_THAN, '6')
        self.assertFalse(cond_b.is_equals())

    def test_is_less_than(self) -> None:

        cond = Condition('Height', Comparision.LESS_THAN, '66')
        self.assertTrue(cond.is_less_than())

        cond_b = Condition('Height', Comparision.GREATER_THAN, '66')
        self.assertFalse(cond_b.is_less_than())

    def test_is_greater_than(self) -> None:

        cond = Condition('Height', Comparision.GREATER_THAN, '66')
        self.assertTrue(cond.is_greater_than())

        cond_b = Condition('Height', Comparision.EQUALS, '66')
        self.assertFalse(cond_b.is_greater_than())