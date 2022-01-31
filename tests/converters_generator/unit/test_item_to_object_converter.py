from converters_generator.domain.item_to_object_converter_generator import ItemToObjectConverterGenerator
from tests.converters_generator.utils import class_file_contents_mother


def test_returns_converter_with_proper_file_name():
    class_file_contents = class_file_contents_mother.get_class_file_contents()
    converter_generator = ItemToObjectConverterGenerator()
    converter = converter_generator.generate(class_file_contents)
    converter_has_proper_file_name = converter.file_name == "item_to_example_converter.py"
    assert converter_has_proper_file_name


def test_returns_converter_with_proper_file_contents():
    class_file_contents = class_file_contents_mother.get_class_file_contents()
    converter_generator = ItemToObjectConverterGenerator()
    converter = converter_generator.generate(class_file_contents)
    expected_converter_file_contents = """def convert(example_item: ExampleItem) -> Example:
    return Example(
        example_item.int_,
        example_item.float_,
        example_item.str_,
        example_item.list_,
    )"""
    converter_has_proper_file_contents = converter.file_contents == expected_converter_file_contents
    assert converter_has_proper_file_contents
