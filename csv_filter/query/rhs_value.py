from csv_filter.query.rhs import RHS

class RHSValue(RHS):

    def __init__(self, value) -> None:
        v = self._cast_to_numeric(value=value)
        super().__init__(value=v)

    def is_value(self) -> bool:
        return True

    def is_list(self) -> bool:
        return False
