from converters_generator.domain.utils.class_attributes_retriever import get_class_attributes
from converters_generator.domain.utils.class_name_retriever import get_class_name
from converters_generator.domain.converter import Converter
from converters_generator.domain.converter_generator import ConverterGenerator


class MongoObjectToObjectConverterGenerator(ConverterGenerator):
    def generate(self, class_file_contents: str) -> Converter:
        class_name = get_class_name(class_file_contents)
        file_name = self.__get_file_name(class_name)
        file_contents = self.__get_file_contents(class_name, class_file_contents)
        converter = Converter(file_name, file_contents)
        return converter

    @staticmethod
    def __get_file_name(class_name: str) -> str:
        class_name = class_name.lower()
        file_name = f"mongo_object_to_{class_name}_converter.py"
        return file_name

    @staticmethod
    def __get_file_contents(class_name: str, class_file_contents: str) -> str:
        class_attributes = get_class_attributes(class_file_contents)
        first_function_definition = f"def convert_many({class_name.lower()}s_as_dict: List[dict]) -> List[{class_name}]:"
        first_function_implementation = f"    return [convert({class_name.lower()}_as_dict) for {class_name.lower()}_as_dict in {class_name.lower()}s_as_dict]"
        second_function_definition = f"def convert({class_name.lower()}_as_dict: dict) -> {class_name}:"
        object_instantiation_first_line = f"    return {class_name}("
        object_instantiation_middle_lines = [
            f"        example_as_dict[\"{attribute}\"]," for attribute in class_attributes
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
