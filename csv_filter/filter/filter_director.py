from abc import ABC, abstractmethod

from csv_filter.filter.table_filter import TableFilter

"""
    Directs the building of a TableFilter using a FilterBuilder
"""
class FilterDirector(ABC):

    @abstractmethod
    def generate(self) -> TableFilter:
        pass