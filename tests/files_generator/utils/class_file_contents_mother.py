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
