import pandas as pd

from csv_filter.parse.table_filter import TableFilter

"""
    Controls the overall process of filtering the input csv file
"""
class ProcessService:

    def run(self, path:str, filter:TableFilter) -> str:
        """
            read the file into a data frame
            apply the filters
            return the filtered csv as a string (or write to a file?)
        """

        df = pd.read_csv(filepath_or_buffer=path)

        filtered_df = filter.apply_filters(df)

        return filtered_df.to_csv()
