import unittest

from csv_filter.parse.cli_parser import CliParser

class CliParserTest(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        self._parser = CliParser()

    def test_parse_one_condition_simple(self) -> None:

        condition='A=2'
        self._parser.parse([condition])

        self.assertEqual(1, self._parser.condition_count())
        condition = self._parser.condition(0)
        self.assertEqual('A', condition.lhs)
        self.assertEqual('=', condition.op)
        self.assertEqual('2', condition.rhs)