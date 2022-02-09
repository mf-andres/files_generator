from files_generator.domain.mongo_object_to_object_file_generator import MongoObjectToObjectFileGenerator
from tests.files_generator.utils import class_file_contents_mother


def test_returns_file_with_proper_file_name():
    class_file_contents = class_file_contents_mother.get_class_file_contents()
    file_generator = MongoObjectToObjectFileGenerator()
    file = file_generator.generate(class_file_contents)
    file_has_proper_file_name = file.file_name == "mongo_object_to_example_converter.py"
    assert file_has_proper_file_name


def test_returns_file_with_proper_file_contents():
    class_file_contents = class_file_contents_mother.get_class_file_contents()
    file_generator = MongoObjectToObjectFileGenerator()
    file = file_generator.generate(class_file_contents)
    expected_file_file_contents = """def convert_many(examples_as_dict: List[dict]) -> List[Example]:
    return [convert(example_as_dict) for example_as_dict in examples_as_dict]


def convert(example_as_dict: dict) -> Example:
    return Example(
        example_as_dict["int_"],
        example_as_dict["float_"],
        example_as_dict["str_"],
        example_as_dict["list_"],
    )"""
    file_has_proper_file_contents = file.file_contents == expected_file_file_contents
    assert file_has_proper_file_contents
