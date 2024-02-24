import unittest

from csv_filter.parse.cli_parser import CliParser
from csv_filter.filter.single_condition_filter import SingleConditionFilter
from csv_filter.filter.two_condition_filter import TwoConditionFilter

from csv_filter.query.operator import Operator

from csv_filter.parse.condition_parser import ConditionParser
from csv_filter.filter.table_filter_builder import TableFilterBuilder

class CliParserTest(unittest.TestCase):

    def test_parse_one_condition_simple(self) -> None:

        args = [
            ['w3','=','q'],
            ["TRANSACTION DETAILS", '=','BIG BANK CORP']
        ]

        for arg_list in args:
            arg = ''.join(arg_list)

            parser = CliParser(args=[arg], parser=ConditionParser(), builder=TableFilterBuilder())
            result = parser.generate()
            self.assertIsInstance(result, SingleConditionFilter)

    def test_parse_one_condition_simple_numerics(self) -> None:

        args = [
            ['A','=','2'],
            ['Z','>','5'],
            ['q','<','0'],
            ["ACCOUNT BALANCE", '=','500.0'],
        ]

        for arg_list in args:
            arg = ''.join(arg_list)

            parser = CliParser(args=[arg], parser=ConditionParser(), builder=TableFilterBuilder())
            result = parser.generate()
            self.assertIsInstance(result, SingleConditionFilter)


    def test_parse_one_condition_multi_value(self) -> None:

        args = [
            ['A','=',['2','3','7']],
            ['w3','=',['q','3','a','w','t']],
            ['Z','>',['5','000','4e3w']]
        ]

        for arg_list in args:
            rhs = ','.join(arg_list[2])
            arg = ''.join([arg_list[0], arg_list[1], rhs])

            parser = CliParser(args=[arg], parser=ConditionParser(), builder=TableFilterBuilder())
            result = parser.generate()
            self.assertIsInstance(result, SingleConditionFilter)


    def test_parse_two_conditions(self) -> None:
        args = [
            [['A B','=','2'], Operator.OR.value, ['Bingo Yule','=','Yes']],
            [['w3','<','99'], Operator.AND.value, ['wiggle', '=', 'f']]
        ]

        for arg_list in args:

            c_1 = ''.join(arg_list[0])

            c_2 = ''.join(arg_list[2])

            parser = CliParser(args=[c_1, arg_list[1], c_2], parser=ConditionParser(), builder=TableFilterBuilder())
            result = parser.generate()

            self.assertIsInstance(result, TwoConditionFilter)
