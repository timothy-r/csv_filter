from csv_filter.parse.filter_generator import FilterGenerator
from csv_filter.filter.table_filter import TableFilter
from csv_filter.filter.table_filter_builder import TableFilterBuilder

from csv_filter.parse.condition_parser import ConditionParser

from csv_filter.query.operator import Operator

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
        condition_parser = ConditionParser()
        builder = TableFilterBuilder()
        index = 0

        for arg in self._args:
            if (index % 2 == 0):
                builder.add_condition(
                    condition_parser.parse(arg=arg)
                )
            else:
                op = Operator.from_str(arg)
                builder.add_operator(operator=op)

            index += 1

        return builder.build()