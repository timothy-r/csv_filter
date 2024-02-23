from dependency_injector import containers, providers

from csv_filter.parse.cli_parser import CliParser
from csv_filter.process.process_service import ProcessService

class Container(containers.DeclarativeContainer):

    cli_parser = providers.Factory(
        CliParser
    )

    filter = providers.Singleton(
        ProcessService,
        parser=cli_parser
    )