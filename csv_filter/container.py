from dependency_injector import containers, providers

from csv_filter.parse.cli_args_director import CliArgsDirector
from csv_filter.parse.condition_parser import ConditionParser

from csv_filter.process.process_service import ProcessService
from csv_filter.filter.table_filter_builder import TableFilterBuilder



class Container(containers.DeclarativeContainer):


    condition_parser = providers.Factory(
        ConditionParser
    )

    process_service = providers.Singleton(
        ProcessService
    )

    table_filter_builder = providers.Factory(
        TableFilterBuilder
    )

    cli_args_director = providers.Factory(
        CliArgsDirector,
        builder=table_filter_builder,
        parser=condition_parser
    )