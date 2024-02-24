import unittest

from csv_filter.parse.condition_parser import ConditionParser

from csv_filter.query.comparison import Comparision

class ConditionParserTest(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        self._parser = ConditionParser()

    def test_parse_one_condition_simple(self) -> None:

        args = [
            ['w3','=','q'],
            ["TRANSACTION DETAILS", '=','BIG BANK CORP']
        ]

        for arg_list in args:
            arg = ''.join(arg_list)

            condition = self._parser.parse(arg=arg)

            self.assertEqual(arg_list[0], condition.lhs)
            comp = Comparision.from_str(arg_list[1])
            self.assertEqual(comp, condition.comparison)
            self.assertEqual(arg_list[2], condition.rhs.value)

    def test_parse_one_condition_simple_integers(self) -> None:

        args = [
            ['A','=','2'],
            ['Z','>','5'],
            ['q','<','0']        ]

        for arg_list in args:
            arg = ''.join(arg_list)

            condition = self._parser.parse(arg=arg)

            self.assertEqual(arg_list[0], condition.lhs)
            comp = Comparision.from_str(arg_list[1])
            self.assertEqual(comp, condition.comparison)
            self.assertEqual(int(arg_list[2]), condition.rhs.value)

    def test_parse_one_condition_simple_floats(self) -> None:

        args = [
            ['A','=','2.7'],
            ['Z','>','50.22'],
            ['q','<','0.000034'],
            ["ACCOUNT BALANCE", '=','500.0'],
        ]

        for arg_list in args:
            arg = ''.join(arg_list)

            condition = self._parser.parse(arg=arg)

            self.assertEqual(arg_list[0], condition.lhs)
            comp = Comparision.from_str(arg_list[1])
            self.assertEqual(comp, condition.comparison)
            self.assertEqual(float(arg_list[2]), condition.rhs.value)


    def test_parse_one_condition_multi_value(self) -> None:

        args = [
            ['w3','=',['q','z','a','w','t']],
        ]

        for arg_list in args:
            rhs = ','.join(arg_list[2])
            arg = ''.join([arg_list[0], arg_list[1], rhs])

            condition = self._parser.parse(arg=arg)

            self.assertEqual(arg_list[0], condition.lhs)
            comp = Comparision.from_str(arg_list[1])
            self.assertEqual(comp, condition.comparison)
            self.assertEqual(arg_list[2], condition.rhs.value)

    def test_parse_one_condition_multi_value_ints(self) -> None:

        args = [
            ['A','=',['2','3','7']],
            ['Z','>',['5','0','43125']],
            ['Yep','<',['5','0','43125']]
        ]

        for arg_list in args:
            rhs = ','.join(arg_list[2])
            arg = ''.join([arg_list[0], arg_list[1], rhs])

            condition = self._parser.parse(arg=arg)

            self.assertEqual(arg_list[0], condition.lhs)
            comp = Comparision.from_str(arg_list[1])
            self.assertEqual(comp, condition.comparison)
            expected = [
                int(x) for x in arg_list[2]
            ]
            self.assertEqual(expected, condition.rhs.value)

    def test_parse_one_condition_multi_value_floats(self) -> None:

        args = [
            ['A','=',['2.334','30234.012','7.7']],
        ]

        for arg_list in args:
            rhs = ','.join(arg_list[2])
            arg = ''.join([arg_list[0], arg_list[1], rhs])

            condition = self._parser.parse(arg=arg)

            self.assertEqual(arg_list[0], condition.lhs)
            comp = Comparision.from_str(arg_list[1])
            self.assertEqual(comp, condition.comparison)
            expected = [
                float(x) for x in arg_list[2]
            ]
            self.assertEqual(expected, condition.rhs.value)