import pandas as pd

from csv_filter.parse.cli_args_director import CliArgsDirector
from csv_filter.filter.filter_director import FilterDirector

"""
    Controls the overall process of filtering the input csv file
"""
class ProcessService:

    def run(self, path:str, director:FilterDirector) -> str:
        """
            read the file into a data frame
            apply the filters
            return the filtered results as a string (or write to a file?)
        """

        df = pd.read_csv(filepath_or_buffer=path)

        filter = director.generate()

        filtered_df = filter.apply_filters(df)

        return filtered_df.to_csv()
