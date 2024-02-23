import unittest

from csv_filter.parse.cli_parser import CliParser

class CliParserTest(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        self._parser = CliParser()

    def test_parse_one_condition_simple(self) -> None:

        args = [
            ['A','=','2'],
            ['w3','=','q'],
            ['Z','>','5'],
            ['q','<','0'],
            ["ACCOUNT BALANCE", '=','500.0']
        ]

        for arg_list in args:
            arg = ''.join(arg_list)

            self._parser.parse([arg])
            self.assertEqual(1, self._parser.condition_count())
            self.assertEqual(0, self._parser.operator_count())
            condition = self._parser.condition(0)

            self.assertEqual(arg_list[0], condition.lhs)
            self.assertEqual(arg_list[1], condition.comparison)
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

            self._parser.parse([arg])
            self.assertEqual(1, self._parser.condition_count())
            self.assertEqual(0, self._parser.operator_count())
            condition = self._parser.condition(0)

            self.assertEqual(arg_list[0], condition.lhs)
            self.assertEqual(arg_list[1], condition.comparison)
            self.assertEqual(arg_list[2], condition.rhs)

    def test_parse_two_conditions(self) -> None:
        args = [
            [['A','=','2'], CliParser.OP_OR,['Bingo','=','Yes']],
            [['w3','<','99'], CliParser.OP_AND, ['wiggle', '=', 'f']]
        ]

        for arg_list in args:

            c_1 = ''.join(arg_list[0])

            c_2 = ''.join(arg_list[2])

            self._parser.parse([c_1, arg_list[1], c_2])
            self.assertEqual(2, self._parser.condition_count())
            self.assertEqual(1, self._parser.operator_count())

            operator = self._parser.operator(0)
            self.assertEqual(arg_list[1], operator)