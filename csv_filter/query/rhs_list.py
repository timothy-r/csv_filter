from csv_filter.query.rhs import RHS

class RHSList(RHS):

    def __init__(self, value) -> None:
        v = [
            self._cast_to_numeric(value=x) for x in value
        ]
        super().__init__(value=v)

    def is_value(self) -> bool:
        return False

    def is_list(self) -> bool:
        return True

