from abc import ABC, abstractmethod

from csv_filter.pandas_filter.pandas_table_filter import PandasTableFilter

"""
    Directs the building of a TableFilter using a FilterBuilder
"""
class FilterDirector(ABC):

    @abstractmethod
    def generate(self) -> PandasTableFilter:
        pass