from files_generator.domain.file import File
from files_generator.domain.file_generator import FileGenerator
from files_generator.domain.utils.class_attributes_retriever import get_class_attributes_names_and_types
from files_generator.domain.utils.class_name_retriever import get_class_name


class ItemToObjectFileGenerator(FileGenerator):
    def generate(self, class_file_contents: str) -> File:
        class_name = get_class_name(class_file_contents)
        file_name = self.__get_file_name(class_name)
        file_contents = self.__get_file_contents(class_name, class_file_contents)
        file = File(file_name, file_contents)
        return file

    @staticmethod
    def __get_file_name(class_name: str) -> str:
        class_name = class_name.lower()
        file_name = f"item_to_{class_name}_converter.py"
        return file_name

    @staticmethod
    def __get_file_contents(class_name: str, class_file_contents: str) -> str:
        class_attributes_names_and_types = get_class_attributes_names_and_types(class_file_contents)
        function_definition = f"def convert({class_name.lower()}_item: {class_name}Item) -> {class_name}:"
        object_instantiation_first_line = f"    return {class_name}("
        object_instantiation_middle_lines = [
            f"        {class_name.lower()}_item.{name}," for name, type in class_attributes_names_and_types
        ]
        object_instantiation_last_line = "    )"
        file_contents = "\n".join(
            [function_definition, object_instantiation_first_line]
            + object_instantiation_middle_lines
            + [object_instantiation_last_line]
        )
        return file_contents
