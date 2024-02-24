import re

from csv_filter.query.condition import Condition
from csv_filter.query.comparison import Comparision

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
                rhs = self._cast_to_numeric(matches.group(3))
            else:
                rhs = [
                    self._cast_to_numeric(x) for x in items
                ]

            comp = Comparision.from_str(matches.group(2))

            return Condition(lhs=matches.group(1), comparison=comp, rhs=rhs)
        else:
            raise ValueError('Invalid arg "{}"'.format(arg))

    def _cast_to_numeric(self, value:str):
        """
            attemprt to convert value parameter to either an int or a float
        """
        try:
            return int(value)
        except:
            pass

        try:
            return float(value)
        except:
            pass

        return value
