
from csv_filter.filter.table_filter import TableFilter
from csv_filter.filter.single_condition_list_filter import SingleConditionListFilter
from csv_filter.filter.single_condition_value_filter import SingleConditionValueFilter
from csv_filter.filter.two_condition_values_and_filter import TwoConditionValuesAndFilter

from csv_filter.parse.condition import Condition
from csv_filter.parse.operator import Operator

class TableFilterBuilder:

    def __init__(self) -> None:
        self._conditions = []
        self._operators = []

    def add_operator(self, operator:Operator) -> None:
        self._operators.append(operator)

    def add_condition(self, condition:Condition) -> None:
        self._conditions.append(condition)

    def build(self) -> TableFilter:
        """
            using the conditions and operators build a TableFilter instance
        """
        if len(self._conditions) == 1 and len(self._operators) == 0:
            condition = self._conditions[0]
            if condition.rhs_is_value():
                return SingleConditionValueFilter(condition=condition)
            elif condition.rhs_is_list():
                return SingleConditionListFilter(condition=condition)

        elif len(self._conditions) == 2 and len(self._operators) == 1:
            cond_a = self._conditions[0]
            op = self._operators[0]
            cond_b = self._conditions[1]

            if op == Operator.AND:
                # test each condition
                if cond_a.rhs_is_value() and cond_b.rhs_is_value():
                    return TwoConditionValuesAndFilter(a=cond_a, b=cond_b)
            elif op == Operator.OR:
                pass