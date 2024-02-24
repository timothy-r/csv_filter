import re

from csv_filter.query.condition import Condition
from csv_filter.query.comparison import Comparision
from csv_filter.query.rhs_list import RHSList
from csv_filter.query.rhs_value import RHSValue

class ConditionParser:

    def __init__(self) -> None:
        valid_comparisons = ''.join(Comparision.valid_comparisons())
        self._pattern = "(.*)([{}])(.*)".format(valid_comparisons)

    def parse(self, arg:str) -> Condition:
        """
            split arg into 3 parts lhs, comparison, rhs
            and create a Condition instance
        """

        matches = re.match(pattern=self._pattern, string=arg)

        if len(matches.groups()) == 3:
            # split rhs on comma
            items = matches.group(3).split(',')

            if len(items) == 1:
                rhs = RHSValue(matches.group(3))
            else:
                rhs = RHSList(items)

            comp = Comparision(matches.group(2))

            return Condition(lhs=matches.group(1), comparison=comp, rhs=rhs)
        else:
            raise ValueError('Invalid arg "{}"'.format(arg))
