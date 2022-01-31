from converters_generator.domain.converter import Converter
from converters_generator.domain.converter_generator import ConverterGenerator


class ItemToObjectConverterGenerator(ConverterGenerator):
    def generate(self, class_file_contents: str) -> Converter:
        file_name = self.__get_file_name(class_file_contents)
        file_contents = ""
        converter = Converter(file_name, file_contents)
        return converter

    def __get_file_name(self, class_file_contents: str) -> str:
        class_name_position = self.__get_word_end_index(class_file_contents, "class") + 1
        colon_position = class_file_contents.find(":")
        class_name = class_file_contents[class_name_position + 1: colon_position]
        class_name = class_name.lower()
        file_name = f"item_to_{class_name}_converter.py"
        return file_name

    def __get_word_end_index(self, str_: str, word: str):
        word_end_index = str_.find(word) + len(word) - 1
        return word_end_index
