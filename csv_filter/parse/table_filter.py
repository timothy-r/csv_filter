import pandas as pd

from csv_filter.parse.condition import Condition
from csv_filter.parse.operator import Operator
from csv_filter.parse.comparison import Comparision

"""
    Class that encapsulates the filters to apply to a pandas data frame
"""
class TableFilter:

    OP_AND = 'and'
    OP_OR = 'or'

    def __init__(self) -> None:
        self._conditions = []
        self._operators = []

    def add_condition(self, condition:Condition) -> None:
        self._conditions.append(condition)

    def condition(self, index:int) -> Condition:
        if index < len(self._conditions):
            return self._conditions[index]

    def condition_count(self) -> int:
        return len(self._conditions)

    def add_operator(self, operator:Operator) -> None:
        self._operators.append(operator)

    def operator(self, index:int) -> str:
        if index < len(self._operators):
            return self._operators[index]

    def operator_count(self) -> int:
        return len(self._operators)

    def apply_filters(self, df:pd.DataFrame) -> pd.DataFrame:
        """
            apply the set filters to the parameter data frame and return the result
        """
        ops = len(self._operators)
        if 0 == ops:
            return self._apply_single_condition(df=df)
        elif 1 == ops:
            return self._apply_two_conditions(df=df)
        else:
            return df

    def _apply_single_condition(self, df:pd.DataFrame) -> pd.DataFrame:

            condition = self._conditions[0]
            lhs = condition.lhs

            if type(condition.rhs) == str:
                if condition.comparison == Comparision.EQUALS:
                    df = df.loc[df[lhs] == condition.rhs]
                elif condition.comparison == Comparision.GREATER_THAN:
                    df = df.loc[df[lhs] > condition.rhs]
                elif condition.comparison == Comparision.LESS_THAN:
                    df = df.loc[df[lhs] < condition.rhs]

            elif type(condition.rhs) == list:
                if condition.comparison == Comparision.EQUALS:
                    df = df.loc[df[lhs].isin(condition.rhs)]
                else:
                    raise TypeError
            else:
                raise TypeError

            return df

    def _apply_two_conditions(self, df:pd.DataFrame) -> pd.DataFrame:
        condition_1 = self._conditions[0]
        operator = self._operators[0]
        condition_2 = self._conditions[1]

        # need to use condition.comparison as well
        if type(condition_1.rhs) == str and type(condition_2.rhs) == str and operator == Operator.AND:
            df = df.loc[(df[condition_1.lhs] == condition_1.rhs) & (df[condition_2.lhs] == condition_2.rhs)]
        else:
            raise TypeError


        return df
