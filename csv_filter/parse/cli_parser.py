from csv_filter.parse.filter_generator import FilterGenerator
from csv_filter.filter.table_filter import TableFilter
from csv_filter.filter.table_filter_builder import TableFilterBuilder

from csv_filter.parse.condition_parser import ConditionParser

from csv_filter.query.operator import Operator

"""
    Class that parses a list of arguments into a format to use to build a filter
    Acts as the director in the builder design pattern
"""
class CliParser(FilterGenerator):

    def __init__(self, args:list, builder:TableFilterBuilder, parser:ConditionParser) -> None:
        self._args = args
        self._builder = builder
        self._parser = parser

    def generate(self) -> TableFilter:
        """
            parse the args from the cli into a TableFilter instance
        """
        index = 0

        for arg in self._args:
            if (index % 2 == 0):
                self._builder.add_condition(
                    self._parser.parse(arg=arg)
                )
            else:
                op = Operator.from_str(arg)
                self._builder.add_operator(operator=op)

            index += 1

        return self._builder.build()