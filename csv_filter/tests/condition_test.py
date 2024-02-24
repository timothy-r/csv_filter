import unittest

from csv_filter.query.condition import Condition
from csv_filter.query.comparison import Comparision
from csv_filter.query.rhs_list import RHSList
from csv_filter.query.rhs_value import RHSValue

class ConditionTest(unittest.TestCase):

    def test_is_equals(self) -> None:

        rhs = RHSValue('4')
        cond = Condition(lhs='A', comparison=Comparision.EQUALS, rhs=rhs)
        self.assertTrue(cond.is_equals())

        rhs_b = RHSValue('4')
        cond_b = Condition(lhs='X', comparison=Comparision.LESS_THAN, rhs=rhs_b)
        self.assertFalse(cond_b.is_equals())

    def test_is_less_than(self) -> None:

        rhs = RHSValue('66')
        cond = Condition(lhs='Height', comparison=Comparision.LESS_THAN, rhs=rhs)
        self.assertTrue(cond.is_less_than())

        rhs_b = RHSValue('66')
        cond_b = Condition(lhs='Height', comparison=Comparision.GREATER_THAN, rhs=rhs_b)
        self.assertFalse(cond_b.is_less_than())

    def test_is_greater_than(self) -> None:

        rhs = RHSValue('66')
        cond = Condition(lhs='Height', comparison=Comparision.GREATER_THAN, rhs=rhs)
        self.assertTrue(cond.is_greater_than())

        cond_b = Condition(lhs='Height', comparison=Comparision.EQUALS, rhs=rhs)
        self.assertFalse(cond_b.is_greater_than())

    def test_rhs_is_value(self) -> None:

        rhs = RHSValue('66')
        cond = Condition(lhs='Height', comparison=Comparision.GREATER_THAN, rhs=rhs)
        self.assertTrue(cond.rhs_is_value())

        rhs_b = RHSList(['66', '777'])
        cond_b = Condition(lhs='Height', comparison=Comparision.EQUALS, rhs=rhs_b)
        self.assertFalse(cond_b.rhs_is_value())

    def test_rhs_is_list(self) -> None:

        rhs = RHSList(['99', '6663'])
        cond = Condition(lhs='Height', comparison=Comparision.GREATER_THAN, rhs=rhs)
        self.assertTrue(cond.rhs_is_list())

        rhs_b = RHSValue('777')
        cond_b = Condition(lhs='Height', comparison=Comparision.EQUALS, rhs=rhs_b)
        self.assertFalse(cond_b.rhs_is_list())
