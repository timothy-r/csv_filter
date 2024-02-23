import pandas as pd
from csv_filter.parse.cli_parser import CliParser

class ProcessService:

    def __init__(self, parser:CliParser) -> None:
        self._parser = parser

    def run(self, path:str, args:list) -> str:

        df = pd.read_csv(filepath_or_buffer=path)

        filtered_df = df

        self._parser.parse(args=args)

        ops = self._parser.operator_count()
        if ops == 0:

            # single condition

            condition = self._parser.condition(0)
            lhs = condition.lhs

            if type(condition.rhs) == str:
                if condition.comparison == CliParser.EQUALS:
                    filtered_df = df.loc[df[lhs] == condition.rhs]
                elif condition.comparison == CliParser.GREATER_THAN:
                    filtered_df = df.loc[df[lhs] > condition.rhs]
                elif condition.comparison == CliParser.LESS_THAN:
                    filtered_df = df.loc[df[lhs] < condition.rhs]

            elif type(condition.rhs) == list:
                pass
            else:
                raise TypeError
        elif ops == 1:
            # 2 conditions
            pass
        else:
            raise ValueError("More than 1 operator is not supported")

        return filtered_df.to_csv()