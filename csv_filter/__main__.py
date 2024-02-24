import sys
from typing import Callable

from dependency_injector.wiring import Provide, inject

from csv_filter.container import Container
from csv_filter.process.process_service import ProcessService
from csv_filter.filter.filter_director import FilterDirector

@inject
def main(
    path:str,
    args:list,
    director_factory:Callable[..., FilterDirector] = Provide[Container.cli_args_director.provider],
    process_service: ProcessService = Provide[Container.process_service]
    ) -> None:

    try:

        director = director_factory(args=args)

        result = process_service.run(
            path=path,
            director=director
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