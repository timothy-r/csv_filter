import re
from collections import namedtuple

Condition = namedtuple("Condition", "lhs op rhs")

"""
    Class to parse a list of arguments into a format to use to build a filter
"""
class CliParser:

    def parse(self, args:list) -> None:
        self._args = args
        self._conditions = []
        self._operators = []

        index = 0

        for arg in args:
            if (index % 2 == 0):
                self._conditions.append(self._parse_condition(arg))
            else:
                self._operators.append(arg)

            index += 1

    def condition(self, index:int) -> Condition:
        if index < len(self._conditions):
            return self._conditions[index]

    def condition_count(self) -> int:
        return len(self._conditions)

    def operator_count(self) -> int:
        pass

    def _parse_condition(self, arg:str):
        """
            split arg into 3 parts lhs, op, rhs
                valid ops are = < >
            split rhs on comma
        """

        matches = re.match("(\w+)(\W)(.*)", arg)

        if len(matches.groups()) == 3:
            # split rhs on comma
            rhs = matches.group(3).split(',')
            if len(rhs) == 1:
                rhs = matches.group(3)
            return Condition(lhs=matches.group(1),op=matches.group(2), rhs=rhs)
        else:
            raise ValueError