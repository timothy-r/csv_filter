from enum import Enum

class Operator(Enum):
    AND = 'and'
    OR = 'or'

    @staticmethod
    def from_str(value:str) -> "Operator":
        if value == Operator.AND.value:
            return Operator.AND
        elif value == Operator.OR.value:
            return Operator.OR
        else:
            raise ValueError("Invalid operator: {}".format(arg))