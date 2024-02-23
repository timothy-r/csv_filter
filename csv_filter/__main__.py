import sys
from dependency_injector.wiring import Provide, inject

from csv_filter.container import Container
from csv_filter.process.process_service import ProcessService

@inject
def main(
    path:str,
    args:list,
    filter: ProcessService = Provide[Container.filter]
    ) -> None:

    result = filter.run(path=path, args=args)

    # print its response
    print(result)

if __name__ == "__main__":

    container = Container()
    container.init_resources()
    container.wire(modules=[__name__])

    args = sys.argv
    # remove the module name
    args.pop(0)
    path = args.pop(0)

    main(path=path, args=args)