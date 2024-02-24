
from csv_filter.filter.table_filter import TableFilter
from csv_filter.filter.single_condition_filter import SingleConditionFilter
from csv_filter.filter.two_condition_filter import TwoConditionFilter

from csv_filter.query.condition import Condition
from csv_filter.query.operator import Operator

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
            return SingleConditionFilter(condition=self._conditions[0])

        elif len(self._conditions) == 2 and len(self._operators) == 1:
            cond_a = self._conditions[0]
            op = self._operators[0]
            cond_b = self._conditions[1]

            if op == Operator.AND:
                # test each condition
                if cond_a.rhs_is_value() and cond_b.rhs_is_value():
                    return TwoConditionFilter(a=cond_a, b=cond_b)
            elif op == Operator.OR:
                pass