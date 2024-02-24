from abc import ABC, abstractmethod

"""
    Applies condition filters to data
    With one or more conditions
"""
class Filter(ABC):

    @abstractmethod
    def apply_filters(self):
        pass