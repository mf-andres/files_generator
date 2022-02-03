from converters_generator.domain.mongo_object_to_object_converter_generator import MongoObjectToObjectConverterGenerator
from tests.converters_generator.utils import class_file_contents_mother


def test_returns_converter_with_proper_file_name():
    class_file_contents = class_file_contents_mother.get_class_file_contents()
    converter_generator = MongoObjectToObjectConverterGenerator()
    converter = converter_generator.generate(class_file_contents)
    converter_has_proper_file_name = converter.file_name == "mongo_object_to_example_converter.py"
    assert converter_has_proper_file_name


def test_returns_converter_with_proper_file_contents():
    class_file_contents = class_file_contents_mother.get_class_file_contents()
    converter_generator = MongoObjectToObjectConverterGenerator()
    converter = converter_generator.generate(class_file_contents)
    expected_converter_file_contents = """def convert_many(examples_as_dict: List[dict]) -> List[Example]:
    return [convert(example_as_dict) for example_as_dict in examples_as_dict]


def convert(example_as_dict: dict) -> Example:
    return Example(
        example_as_dict["int_"],
        example_as_dict["float_"],
        example_as_dict["str_"],
        example_as_dict["list_"],
    )"""
    converter_has_proper_file_contents = converter.file_contents == expected_converter_file_contents
    assert converter_has_proper_file_contents
