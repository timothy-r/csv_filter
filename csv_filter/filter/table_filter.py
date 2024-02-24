import pandas as pd

from abc import ABC, abstractmethod

"""
    Applies a single condition filter to data frames
    With a list of values
"""
class TableFilter(ABC):

    @abstractmethod
    def apply_filters(self, df:pd.DataFrame) -> pd.DataFrame:
        pass