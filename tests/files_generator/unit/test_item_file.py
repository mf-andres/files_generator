from files_generator.domain.item_file_generator import ItemFileGenerator
from tests.files_generator.utils import class_file_contents_mother


def test_returns_file_with_proper_file_name():
    class_file_contents = class_file_contents_mother.get_class_file_contents()
    file_generator = ItemFileGenerator()
    file = file_generator.generate(class_file_contents)
    file_has_proper_file_name = file.file_name == "example_item.py"
    assert file_has_proper_file_name


def test_returns_file_with_proper_file_contents():
    class_file_contents = class_file_contents_mother.get_class_file_contents()
    file_generator = ItemFileGenerator()
    file = file_generator.generate(class_file_contents)
    expected_file_file_contents = """class ExampleItem(BaseModel):
    int_: int
    float_: float
    str_: str
    list_: List[int]
"""
    file_has_proper_file_contents = file.file_contents == expected_file_file_contents
    assert file_has_proper_file_contents
