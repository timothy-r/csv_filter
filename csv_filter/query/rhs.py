from abc import ABC, abstractmethod

"""
    A valid rhs item
"""
class RHS(ABC):

    def __init__(self, value) -> None:
        self._value = value

    @property
    def value(self):
        return self._value

    @abstractmethod
    def is_value(self) -> bool:
        pass

    @abstractmethod
    def is_list(self) -> bool:
        pass

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