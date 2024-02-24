import unittest

import pandas as pd

from csv_filter.filter.table_filter import TableFilter
from csv_filter.filter.single_condition_filter import SingleConditionFilter
from csv_filter.filter.two_condition_filter import TwoConditionFilter

from csv_filter.query.condition import Condition
from csv_filter.query.operator import Operator
from csv_filter.query.comparison import Comparision
from csv_filter.query.rhs_list import RHSList
from csv_filter.query.rhs_value import RHSValue

class TableFilterTest(unittest.TestCase):

    def test_single_condition_value_equals_filter(self) -> None:

        test_df = self.get_bank_account_df()

        rhs = RHSValue('DEB')
        condition = Condition(lhs='Type', comparison=Comparision.EQUALS, rhs=rhs)
        filter = SingleConditionFilter(condition=condition)

        result_df = filter.apply_filters(df=test_df)
        self.assertEqual(3, len(result_df.values))

        for cell in result_df.get('Type'):
            self.assertEqual('DEB', cell)

    def test_single_condition_value_less_than_filter(self) -> None:
        test_df = self.get_bank_account_df()

        rhs = RHSValue('50.0')
        condition = Condition(lhs='Debit Amount', comparison=Comparision.LESS_THAN, rhs=rhs)
        filter = SingleConditionFilter(condition=condition)

        result_df = filter.apply_filters(df=test_df)
        self.assertEqual(3, len(result_df.values))

        for cell in result_df.get('Debit Amount'):
            self.assertTrue(cell < 50.0)

    def test_single_condition_value_greater_than_filter(self) -> None:
        test_df = self.get_bank_account_df()

        rhs = RHSValue('50.0')
        condition = Condition(lhs='Debit Amount', comparison=Comparision.GREATER_THAN, rhs=rhs)
        filter = SingleConditionFilter(condition=condition)

        result_df = filter.apply_filters(df=test_df)
        self.assertEqual(2, len(result_df.values))

        for cell in result_df.get('Debit Amount'):
            self.assertTrue(cell > 50.0)


    def test_single_condition_list_filter(self) -> None:
        test_df = self.get_bank_account_df()

        rhs = RHSList(['DD','FEE'])
        condition = Condition(lhs='Type', comparison=Comparision.EQUALS, rhs=rhs)
        filter = SingleConditionFilter(condition=condition)

        result_df = filter.apply_filters(df=test_df)
        self.assertEqual(2, len(result_df.values))
        for cell in result_df.get('Type'):
            self.assertTrue(cell in ['DD','FEE'])


    def test_two_condition_and_filter(self) -> None:
        test_df = self.get_bank_account_df()
        rhs_a = RHSValue('DEB')
        condition_a = Condition(lhs='Type', comparison=Comparision.EQUALS, rhs=rhs_a)
        operator = Operator.AND
        rhs_b = RHSValue('DELIVEROO')
        condition_b = Condition(lhs='Description', comparison=Comparision.EQUALS, rhs=rhs_b)

        filter = TwoConditionFilter(a=condition_a, b=condition_b, op=operator)

        result_df = filter.apply_filters(df=test_df)
        self.assertEqual(1, len(result_df.values))

    def test_two_condition_less_than_and_filter(self) -> None:
        test_df = self.get_bank_account_df()
        rhs_a = RHSValue('DEB')
        condition_a = Condition(lhs='Type', comparison=Comparision.EQUALS, rhs=rhs_a)
        operator = Operator.AND
        rhs_b = RHSValue('50.0')
        condition_b = Condition(lhs='Debit Amount', comparison=Comparision.LESS_THAN, rhs=rhs_b)

        filter = TwoConditionFilter(a=condition_a, b=condition_b, op=operator)

        result_df = filter.apply_filters(df=test_df)
        self.assertEqual(2, len(result_df.values))

    def test_two_condition_greater_than_and_filter(self) -> None:
        test_df = self.get_bank_account_df()
        rhs_a = RHSValue('DEB')
        condition_a = Condition(lhs='Type', comparison=Comparision.EQUALS, rhs=rhs_a)
        operator = Operator.AND
        rhs_b = RHSValue('50.0')
        condition_b = Condition(lhs='Debit Amount', comparison=Comparision.GREATER_THAN, rhs=rhs_b)

        filter = TwoConditionFilter(a=condition_a, b=condition_b, op=operator)

        result_df = filter.apply_filters(df=test_df)
        self.assertEqual(1, len(result_df.values))

    def test_two_condition_equals_or_filter(self) -> None:
        test_df = self.get_bank_account_df()
        rhs_a = RHSValue('DEB')
        condition_a = Condition(lhs='Type', comparison=Comparision.EQUALS, rhs=rhs_a)
        operator = Operator.OR
        rhs_b = RHSValue('MONTHLY FEE')
        condition_b = Condition(lhs='Description', comparison=Comparision.EQUALS, rhs=rhs_b)

        filter = TwoConditionFilter(a=condition_a, b=condition_b, op=operator)

        result_df = filter.apply_filters(df=test_df)
        self.assertEqual(4, len(result_df.values))



    def get_bank_account_df(self) -> pd.DataFrame:
        """
            create a general purpose df in memory
        """
        cols = ['Date','Type','Account Number','Description','Debit Amount','Credit Amount','Balance']
        values = [
            ['06/02/2024','DEB','00168780','WAITROSE',103.0,'',3500.08],
            ['05/02/2024','DEB','00168780','DELIVEROO',27.5,'',3660.73],
            ['05/02/2024','FEE','00168780','MONTHLY FEE',17.2,'',3702.97],
            ['05/02/2024','DEB','00168780','BREW DOG',38.9,'',3803.51],
            ['04/02/2024','DD','00168780','BARCLAYS MORTGAGE',1238.9,'',5153.42]
        ]

        return pd.DataFrame(values,
                  columns=cols)
