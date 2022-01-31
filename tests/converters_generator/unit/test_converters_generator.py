from converters_generator.application.converters_generator import ConvertersGenerator
from converters_generator.domain.converter import Converter
from tests.converters_generator.utils import class_file_contents_mother


def test_returns_converters():
    converters_generator = ConvertersGenerator()
    class_file_contents = class_file_contents_mother.get_class_file_contents()
    converters = converters_generator.invoke(class_file_contents)
    all_are_converters = all([isinstance(converter, Converter) for converter in converters])
    assert all_are_converters
