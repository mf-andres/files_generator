from files_generator.domain.object_to_mongo_object_file_generator import ObjectToMongoObjectFileGenerator
from tests.files_generator.utils import class_file_contents_mother


def test_returns_file_with_proper_file_name():
    class_file_contents = class_file_contents_mother.get_class_file_contents()
    file_generator = ObjectToMongoObjectFileGenerator()
    file = file_generator.generate(class_file_contents)
    file_has_proper_file_name = file.file_name == "example_to_mongo_object_converter.py"
    assert file_has_proper_file_name


def test_returns_file_with_proper_file_contents():
    class_file_contents = class_file_contents_mother.get_class_file_contents()
    file_generator = ObjectToMongoObjectFileGenerator()
    file = file_generator.generate(class_file_contents)
    expected_file_file_contents = """def convert_many(example_list: List[Example]) -> List[dict]:
    return [convert(example) for example in example_list]


def convert(example: Example) -> dict:
    return {
        \"int_\": example.int_,
        \"float_\": example.float_,
        \"str_\": example.str_,
        \"list_\": example.list_,
    }"""
    file_has_proper_file_contents = file.file_contents == expected_file_file_contents
    assert file_has_proper_file_contents
