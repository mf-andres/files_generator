def get_class_file_contents():
    return """
class Example:
    def __init__(
        self, 
        int_: int, 
        float_: float, 
        str_: str,
        list_: List[int],
    ):
        self.int_ = int_
        self.float_ = float_
        self.str_ = str_
        self.list_ = list_
    """


def get_complex_class_file_contents():
    return """
    class ComplexExample:
        def __init__(
            self, 
            int_: int, 
            float_: float, 
            str_: str,
            list_: List[int],
            datetime_: datetime.datetime,
        ):
            self.int_ = int_
            self.float_ = float_
            self.str_ = str_
            self.list_ = list_
            self.datetime_ = datetime
        """
