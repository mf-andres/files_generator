from converters_generator.domain.item_to_object_converter_generator import ItemToObjectConverterGenerator
from tests.converters_generator.utils import class_file_contents_mother


def test_returns_converter_with_proper_file_name():
    class_file_contents = class_file_contents_mother.get_class_file_contents()
    converter_generator = ItemToObjectConverterGenerator()
    converter = converter_generator.generate(class_file_contents)
    converter_has_proper_file_name = converter.file_name == "item_to_diagnosis_converter.py"
    assert converter_has_proper_file_name
