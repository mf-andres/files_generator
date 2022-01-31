from converters_generator.domain.converter import Converter
from converters_generator.domain.converter_generator import ConverterGenerator


class ObjectToItemConverterGenerator(ConverterGenerator):
    def generate(self, class_file_contents: str) -> Converter:
        class_name = self.__get_class_name(class_file_contents)
        file_name = self.__get_file_name(class_name)
        file_contents = self.__get_file_contents(class_name, class_file_contents)
        converter = Converter(file_name, file_contents)
        return converter

    def __get_class_name(self, class_file_contents: str) -> str:
        class_name_position = self.__get_word_end_index(class_file_contents, "class") + 1
        colon_position = class_file_contents.find(":")
        class_name = class_file_contents[class_name_position + 1: colon_position]
        return class_name

    def __get_file_name(self, class_name: str) -> str:
        class_name = class_name.lower()
        file_name = f"{class_name}_to_item_converter.py"
        return file_name

    def __get_word_end_index(self, str_: str, word: str):
        word_end_index = str_.find(word) + len(word) - 1
        return word_end_index

    def __get_file_contents(self, class_name: str, class_file_contents: str) -> str:
        class_attributes = self.__get_class_attributes(class_file_contents)
        first_function_definition = f"def convert_many({class_name.lower()}_list: List[{class_name}]) -> List[{class_name}Item]:"
        first_function_implementation = f"    return [convert({class_name.lower()}) for {class_name.lower()} in {class_name.lower()}_list]"
        second_function_definition = f"def convert({class_name.lower()}: {class_name}) -> {class_name}Item:"
        object_instantiation_first_line = f"    return {class_name}Item("
        object_instantiation_middle_lines = [
            f"        {attribute}={class_name.lower()}.{attribute}," for attribute in class_attributes
        ]
        object_instantiation_last_line = "    )"
        file_contents = "\n".join(
            [
                first_function_definition,
                first_function_implementation,
                "",
                "",
                second_function_definition,
                object_instantiation_first_line
            ]
            + object_instantiation_middle_lines
            + [object_instantiation_last_line]
        )
        return file_contents

    def __get_class_attributes(self, class_file_contents: str):
        self_end_index = self.__get_word_end_index(class_file_contents, "self,")
        first_attribute_line_index = len(class_file_contents[:self_end_index]) + class_file_contents[
                                                                                 self_end_index:].find("\n") + 1
        end_of_init_function_index = class_file_contents.find("):")
        last_attribute_line_end_index = class_file_contents[:end_of_init_function_index].rfind("\n")
        attributes_definition = class_file_contents[first_attribute_line_index: last_attribute_line_end_index]
        attribute_names = []
        for line in attributes_definition.splitlines():
            colon_index = line.find(":")
            attribute_name = line[:colon_index].strip()
            attribute_names.append(attribute_name)
            comma_index = line.find(",")
            attribute_type = line[colon_index:comma_index].strip()
        return attribute_names
