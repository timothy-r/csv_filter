import unittest

from csv_filter.parse.cli_parser import CliParser
from csv_filter.parse.table_filter import TableFilter
from csv_filter.parse.operator import Operator
from csv_filter.parse.comparison import Comparision
class CliParserTest(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()

    def test_parse_one_condition_simple(self) -> None:

        args = [
            ['A','=','2'],
            ['w3','=','q'],
            ['Z','>','5'],
            ['q','<','0'],
            ["ACCOUNT BALANCE", '=','500.0'],
            ["TRANSACTION DETAILS", '=','BIG BANK CORP']
        ]

        for arg_list in args:
            arg = ''.join(arg_list)

            parser = CliParser(args=[arg])
            result = parser.generate()

            self.assertEqual(1, result.condition_count())
            self.assertEqual(0, result.operator_count())
            condition = result.condition(0)

            self.assertEqual(arg_list[0], condition.lhs)
            comp = Comparision.from_str(arg_list[1])
            self.assertEqual(comp, condition.comparison)
            self.assertEqual(arg_list[2], condition.rhs)

    def test_parse_one_condition_multi_value(self) -> None:

        args = [
            ['A','=',['2','3','7']],
            ['w3','=',['q','3','a','w','t']],
            ['Z','>',['5','000','4e3w']]
        ]

        for arg_list in args:
            rhs = ','.join(arg_list[2])
            arg = ''.join([arg_list[0], arg_list[1], rhs])

            parser = CliParser(args=[arg])
            result = parser.generate()

            self.assertEqual(1, result.condition_count())
            self.assertEqual(0, result.operator_count())
            condition = result.condition(0)

            self.assertEqual(arg_list[0], condition.lhs)
            comp = Comparision.from_str(arg_list[1])
            self.assertEqual(comp, condition.comparison)
            self.assertEqual(arg_list[2], condition.rhs)

    def test_parse_two_conditions(self) -> None:
        args = [
            [['A B','=','2'], Operator.OR.value, ['Bingo Yule','=','Yes']],
            [['w3','<','99'], Operator.AND.value, ['wiggle', '=', 'f']]
        ]

        for arg_list in args:

            c_1 = ''.join(arg_list[0])

            c_2 = ''.join(arg_list[2])

            parser = CliParser(args=[c_1, arg_list[1], c_2])
            result = parser.generate()

            self.assertEqual(2, result.condition_count())
            self.assertEqual(1, result.operator_count())

            operator = result.operator(0)
            if arg_list[1] == Operator.AND:
                self.assertEqual(Operator.AND, operator)
            elif arg_list[1] == Operator.OR:
                self.assertEqual(Operator.OR, operator)