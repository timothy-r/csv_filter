import re
from collections import namedtuple

Condition = namedtuple("Condition", "lhs comparison rhs")

"""
    Class that parses a list of arguments into a format to use to build a filter
"""
class CliParser:

    OP_AND = 'and'
    OP_OR = 'or'

    EQUALS = '='
    GREATER_THAN = '>'
    LESS_THAN = '<'

    def parse(self, args:list) -> None:
        self._args = args
        self._conditions = []
        self._operators = []

        index = 0

        for arg in args:
            if (index % 2 == 0):
                self._conditions.append(self._parse_condition(arg))
            else:
                if arg in [self.OP_AND, self.OP_OR]:
                    self._operators.append(arg)
                else:
                    raise ValueError('Invalid operator "{}"'.format(arg))

            index += 1

    def condition(self, index:int) -> Condition:
        if index < len(self._conditions):
            return self._conditions[index]

    def condition_count(self) -> int:
        return len(self._conditions)

    def operator(self, index:int) -> str:
        if index < len(self._operators):
            return self._operators[index]

    def operator_count(self) -> int:
        return len(self._operators)

    def _parse_condition(self, arg:str):
        """
            split arg into 3 parts lhs, comparison, rhs
            valid op comparisons are = < >
            split rhs on comma
        """

        matches = re.match("(.*)([=<>])(.*)", arg)

        if len(matches.groups()) == 3:
            # split rhs on comma
            rhs = matches.group(3).split(',')
            if len(rhs) == 1:
                rhs = matches.group(3)

            if matches.group(2) in [self.EQUALS, self.GREATER_THAN, self.LESS_THAN]:
                return Condition(lhs=matches.group(1),comparison=matches.group(2), rhs=rhs)
            else:
                raise ValueError('Invalid comparison arg "{}"'.format(matches.group(2)))
        else:
            raise ValueError('Invalid arg "{}"'.format(arg))