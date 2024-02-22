import pandas as pd
from csv_filter.parse.cli_parser import CliParser

class Filter:

    def __init__(self, parser:CliParser) -> None:
        self._parser = parser

    def run(self, path:str, args:list) -> str:

        parsed_args = self._parser.parse(args=args)

        pass