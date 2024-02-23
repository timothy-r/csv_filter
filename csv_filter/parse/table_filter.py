from collections import namedtuple


Condition = namedtuple("Condition", "lhs comparison rhs")

"""
    Class that encapsulates the filters to apply to a table of data (eg csv file)
"""

class TableFilter:

    OP_AND = 'and'
    OP_OR = 'or'

    EQUALS = '='
    GREATER_THAN = '>'
    LESS_THAN = '<'

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

    def add_operator(self, operator:str) -> None:
        if operator in [self.OP_AND, self.OP_OR]:
            self._operators.append(operator)
        else:
            raise ValueError('Invalid operator "{}"'.format(operator))

    def operator(self, index:int) -> str:
        if index < len(self._operators):
            return self._operators[index]

    def operator_count(self) -> int:
        return len(self._operators)

    def valid_comparisons(self) -> list:
        return [TableFilter.LESS_THAN, TableFilter.EQUALS, TableFilter.GREATER_THAN]

