import datetime
from typing import List


class ComplexExample:
    def __init__(
        self,
        int_: int,
        float_: float,
        str_: str,
        list_: List[int],
        datetime_: datetime.datetime,
        list_2: List[float],
    ):
        self.int_ = int_
        self.float_ = float_
        self.str_ = str_
        self.list_ = list_
        self.datetime_ = datetime_
        self.list_2 = list_2
