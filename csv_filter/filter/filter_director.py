from abc import ABC, abstractmethod

from csv_filter.filter.filter import Filter

"""
    Directs the building of a Filter using a FilterBuilder
"""
class FilterDirector(ABC):

    @abstractmethod
    def generate(self) -> Filter:
        pass