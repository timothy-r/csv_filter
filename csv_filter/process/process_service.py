import pandas as pd
from csv_filter.parse.cli_parser import CliParser
from csv_filter.parse.table_filter import TableFilter

"""
    Controls the overall process of filtering the input csv file
"""
class ProcessService:

    def __init__(self, parser:CliParser) -> None:
        self._parser = parser

    def run(self, path:str, args:list) -> str:
        """
            parse the arguments
            read the file into a data frame
            apply the filters
            return the filtered csv as a string (or write to a file?)
        """

        filter = self._parser.parse(args=args)

        df = pd.read_csv(filepath_or_buffer=path)

        filtered_df = self._apply_filters(df, filter=filter)

        return filtered_df.to_csv()

    def _apply_filters(self, df:pd.DataFrame, filter:TableFilter) -> pd.DataFrame:
        """

        """
        ops = filter.operator_count()
        if ops == 0:

            # single condition

            condition = filter.condition(0)
            lhs = condition.lhs

            if type(condition.rhs) == str:
                if condition.comparison == TableFilter.EQUALS:
                    df = df.loc[df[lhs] == condition.rhs]
                elif condition.comparison == TableFilter.GREATER_THAN:
                    df = df.loc[df[lhs] > condition.rhs]
                elif condition.comparison == TableFilter.LESS_THAN:
                    df = df.loc[df[lhs] < condition.rhs]

            elif type(condition.rhs) == list:
                pass
            else:
                raise TypeError
        elif ops == 1:
            # 2 conditions
            pass
        else:
            raise ValueError("More than 1 operator is not supported")

        return df