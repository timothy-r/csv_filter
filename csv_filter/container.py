from dependency_injector import containers, providers

from csv_filter.parse.cli_args_director import CliArgsDirector
from csv_filter.parse.condition_parser import ConditionParser

from csv_filter.process.pandas_process_service import PandasProcessService
from csv_filter.pandas_filter.pandas_table_filter_builder import PandasTableFilterBuilder

class Container(containers.DeclarativeContainer):

    condition_parser = providers.Factory(
        ConditionParser
    )

    pandas_process_service = providers.Singleton(
        PandasProcessService
    )

    table_filter_builder = providers.Factory(
        PandasTableFilterBuilder
    )

    cli_args_director = providers.Factory(
        CliArgsDirector,
        builder=table_filter_builder,
        parser=condition_parser
    )