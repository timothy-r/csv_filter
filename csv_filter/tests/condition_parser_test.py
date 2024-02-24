import unittest

from csv_filter.parse.condition_parser import ConditionParser

from csv_filter.query.comparison import Comparision

class ConditionParserTest(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        self._parser = ConditionParser()

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

            condition = self._parser.parse(arg=arg)

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

            condition = self._parser.parse(arg=arg)

            self.assertEqual(arg_list[0], condition.lhs)
            comp = Comparision.from_str(arg_list[1])
            self.assertEqual(comp, condition.comparison)
            self.assertEqual(arg_list[2], condition.rhs)
