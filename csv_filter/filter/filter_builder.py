from abc import ABC, abstractmethod

from csv_filter.filter.table_filter import TableFilter

from csv_filter.query.condition import Condition
from csv_filter.query.operator import Operator

class FilterBuilder(ABC):

    @abstractmethod
    def add_operator(self, operator:Operator) -> None:
        pass

    @abstractmethod
    def add_condition(self, condition:Condition) -> None:
        pass

    @abstractmethod
    def build(self) -> TableFilter:
        pass