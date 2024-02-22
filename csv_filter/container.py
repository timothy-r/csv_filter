from dependency_injector import containers, providers

from csv_filter.parse.cli_parser import CliParser
from csv_filter.filter.filter import Filter

class Container(containers.DeclarativeContainer):

    cli_parser = providers.Factory(
        CliParser
    )

    filter = providers.Singleton(
        Filter,
        parser=cli_parser
    )