import unittest

from csv_filter.tests.filter_test import FilterTest
from csv_filter.tests.cli_parser_test import CliParserTest
from csv_filter.tests.condition_test import ConditionTest
from csv_filter.tests.table_filter_builder_test import TableFilterBuilderTest
from csv_filter.tests.table_filter_test import TableFilterTest

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    suite = unittest.TestSuite()

    suite.addTest(FilterTest())
    suite.addTest(CliParserTest())
    suite.addTest(ConditionTest())
    suite.addTest(TableFilterBuilderTest())
    suite.addTest(TableFilterTest())

    runner.run(suite)