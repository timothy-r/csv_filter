import sys
from dependency_injector.wiring import Provide, inject

from csv_filter.container import Container
from csv_filter.process.process_service import ProcessService
from csv_filter.parse.cli_parser import CliParser
from csv_filter.parse.condition_parser import ConditionParser

from csv_filter.filter.table_filter_builder import TableFilterBuilder

@inject
def main(
    path:str,
    args:list,
    cli_parser_factory:CliParser = Provide[Container.cli_parser.provider],
    process_service: ProcessService = Provide[Container.process_service]
    ) -> None:

    try:

        cli_parser = cli_parser_factory(args=args)

        result = process_service.run(
            path=path,
            director=cli_parser
        )

        # print its response
        print(result)

    except KeyError as err:
        print("KeyError: key'{}' is invalid".format(err))

if __name__ == "__main__":

    container = Container()
    container.init_resources()
    container.wire(modules=[__name__])

    args = sys.argv
    # remove the module name
    args.pop(0)
    path = args.pop(0)

    main(path=path, args=args)