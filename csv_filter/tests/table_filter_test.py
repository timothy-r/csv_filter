import unittest

import pandas as pd

from csv_filter.filter.table_filter import TableFilter
from csv_filter.filter.single_condition_filter import SingleConditionFilter

from csv_filter.query.condition import Condition
from csv_filter.query.operator import Operator
from csv_filter.query.comparison import Comparision
class TableFilterTest(unittest.TestCase):

    def test_single_condition_value_filter(self) -> None:

        test_df = self.get_bank_account_df()

        condition = Condition(lhs='Type', comparison=Comparision.EQUALS, rhs='DEB')
        filter = SingleConditionFilter(condition=condition)

        result_df = filter.apply_filters(df=test_df)
        self.assertEqual(3, len(result_df.values))

    def test_single_condition_list_filter(self) -> None:
        test_df = self.get_bank_account_df()

        condition = Condition(lhs='Type', comparison=Comparision.EQUALS, rhs=['DD','FEE'])
        filter = SingleConditionFilter(condition=condition)

        result_df = filter.apply_filters(df=test_df)
        self.assertEqual(2, len(result_df.values))


    def get_bank_account_df(self) -> pd.DataFrame:
        """
            create a general purpose df in memory
        """
        cols = ['Date','Type','Account Number','Description','Debit Amount','Credit Amount','Balance']
        values = [
            ['06/02/2024','DEB','00168780','WAITROSE','103.0','','3500.08'],
            ['05/02/2024','DEB','00168780','DELIVEROO','27.5','','3660.73'],
            ['05/02/2024','FEE','00168780','MONTHLY FEE','17.2','','3702.97'],
            ['05/02/2024','DEB','00168780','BREW DOG','38.9','','3803.51'],
            ['04/02/2024','DD','00168780','BARCLAYS MORTGAGE','1238.9','','5153.42']
        ]

        return pd.DataFrame(values,
                  columns=cols)
