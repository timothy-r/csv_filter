from abc import ABC, abstractclassmethod

from csv_filter.filter.filter_director import FilterDirector

"""
    Controls the overall process of filtering the input csv file
    uses pandas to read & filter the data
"""
class ProcessService(ABC):

    @abstractclassmethod
    def run(self, path:str, director:FilterDirector) -> str:
        pass