from files_generator.domain.file_generator import FileGenerator
from files_generator.domain.file import File
from files_generator.domain.utils.class_attributes_retriever import get_class_attributes_names_and_types
from files_generator.domain.utils.class_name_retriever import get_class_name
from files_generator.domain.utils.name_underscorer import underscore_name


class ItemFileGenerator(FileGenerator):
    def generate(self, class_file_contents: str) -> File:
        class_name = get_class_name(class_file_contents)
        file_name = self.__get_file_name(class_name)
        file_contents = self.__get_file_contents(class_name, class_file_contents)
        file = File(file_name, file_contents)
        return file

    # TODO from camel case to python case
    @staticmethod
    def __get_file_name(class_name: str) -> str:
        underscored_class_name = underscore_name(class_name)
        lowered_underscored_class_name = underscored_class_name.lower()
        file_name = f"{lowered_underscored_class_name}_item.py"
        return file_name

    @staticmethod
    def __get_file_contents(class_name: str, class_file_contents: str) -> str:
        class_attributes_and_names = get_class_attributes_names_and_types(class_file_contents)
        class_definition = f"class {class_name}Item(BaseModel):"
        attributes_lines = [
            f"    {attribute_name}: {attribute_type}" for attribute_name, attribute_type in class_attributes_and_names
        ]
        file_contents = "\n".join(
            [class_definition]
            + attributes_lines
            + [""]
        )
        return file_contents
