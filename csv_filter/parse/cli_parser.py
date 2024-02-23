import re

from csv_filter.parse.table_filter import TableFilter, Condition

"""
    Class that parses a list of arguments into a format to use to build a filter
"""
class CliParser:

    def parse(self, args:list) -> TableFilter:
        """
            parse the args from the cli into a TableFilter instance
        """
        table_filter = TableFilter()
        index = 0

        valid_comparisons = ''.join(table_filter.valid_comparisons())

        for arg in args:
            if (index % 2 == 0):
                table_filter.add_condition(
                    self._parse_condition(arg=arg, valid_comparisons=valid_comparisons)
                )
            else:
                table_filter.add_operator(arg)

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

            return Condition(lhs=matches.group(1),comparison=matches.group(2), rhs=rhs)
        else:
            raise ValueError('Invalid arg "{}"'.format(arg))