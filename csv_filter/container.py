from dependency_injector import containers, providers

from csv_filter.parse.cli_parser import CliParser
from csv_filter.process.process_service import ProcessService
from csv_filter.parse.table_filter import TableFilter

class Container(containers.DeclarativeContainer):

    # cli_parser = providers.Factory(
    #     CliParser
    # )

    process_service = providers.Singleton(
        ProcessService
    )