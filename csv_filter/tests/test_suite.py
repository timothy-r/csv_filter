import unittest

from csv_filter.tests.filter_test import FilterTest

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    suite = unittest.TestSuite()

    suite.addTest(FilterTest())

    runner.run(suite)