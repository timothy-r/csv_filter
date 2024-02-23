from abc import ABC, abstractmethod

from csv_filter.parse.table_filter import TableFilter


class FilterGenerator(ABC):

    @abstractmethod
    def generate(self) -> TableFilter:
        pass