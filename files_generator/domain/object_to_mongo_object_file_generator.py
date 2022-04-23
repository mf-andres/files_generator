from files_generator.domain.file import File
from files_generator.domain.file_generator import FileGenerator
from files_generator.domain.utils.class_attributes_retriever import get_class_attributes_names_and_types
from files_generator.domain.utils.class_name_retriever import get_class_name
from files_generator.domain.utils.name_underscorer import underscore_name


class ObjectToMongoObjectFileGenerator(FileGenerator):
    def generate(self, class_file_contents: str) -> File:
        class_name = get_class_name(class_file_contents)
        file_name = self.__get_file_name(class_name)
        file_contents = self.__get_file_contents(class_name, class_file_contents)
        file = File(file_name, file_contents)
        return file

    @staticmethod
    def __get_file_name(class_name: str) -> str:
        underscored_class_name = underscore_name(class_name)
        lowered_underscored_class_name = underscored_class_name.lower()
        file_name = f"{lowered_underscored_class_name}_to_mongo_object_converter.py"
        return file_name

    @staticmethod
    def __get_file_contents(class_name: str, class_file_contents: str) -> str:
        class_attributes_names_and_types = get_class_attributes_names_and_types(class_file_contents)
        first_function_definition = f"def convert_many({class_name.lower()}_list: List[{class_name}]) -> List[dict]:"
        first_function_implementation = f"    return [convert({class_name.lower()}) for {class_name.lower()} in {class_name.lower()}_list]"
        second_function_definition = f"def convert({class_name.lower()}: {class_name}) -> dict:"
        object_instantiation_first_line = "    return {"
        object_instantiation_middle_lines = [
         f"        \"{name}\": {class_name.lower()}.{name}," for name, type in class_attributes_names_and_types
        ]
        object_instantiation_last_line = "    }"
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
