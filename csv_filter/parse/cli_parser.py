import re

from csv_filter.parse.filter_generator import FilterGenerator
from csv_filter.parse.table_filter import TableFilter
from csv_filter.query.condition import Condition
from csv_filter.query.operator import Operator
from csv_filter.query.comparison import Comparision

"""
    Class that parses a list of arguments into a format to use to build a filter
"""
class CliParser(FilterGenerator):

    def __init__(self, args:list) -> None:
        self._args = args

    def generate(self) -> TableFilter:
        """
            parse the args from the cli into a TableFilter instance
        """
        table_filter = TableFilter()
        index = 0

        valid_comparisons = ''.join(Comparision.valid_comparisons())

        for arg in self._args:
            if (index % 2 == 0):
                table_filter.add_condition(
                    self._parse_condition(arg=arg, valid_comparisons=valid_comparisons)
                )
            else:
                op = Operator.from_str(arg)
                if op:
                    table_filter.add_operator(operator=op)
                else:
                    raise ValueError("Invalid operator: {}".format(arg))

            index += 1

        return table_filter

    def _parse_condition(self, arg:str, valid_comparisons:str):
        """
            split arg into 3 parts lhs, comparison, rhs
            valid op comparisons are supplied by the TableFilter
            split rhs on comma
        """
        pattern = "(.*)([{}])(.*)".format(valid_comparisons)

        matches = re.match(pattern=pattern, string=arg)

        if len(matches.groups()) == 3:
            # split rhs on comma
            rhs = matches.group(3).split(',')
            if len(rhs) == 1:
                rhs = matches.group(3)

            comp = Comparision.from_str(matches.group(2))

            return Condition(lhs=matches.group(1), comparison=comp, rhs=rhs)
        else:
            raise ValueError('Invalid arg "{}"'.format(arg))