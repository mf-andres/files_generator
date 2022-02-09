from files_generator.application.files_generator import FilesGenerator
from files_generator.domain.file import File
from tests.files_generator.utils import class_file_contents_mother


def test_returns_file():
    file_generator = FilesGenerator()
    class_file_contents = class_file_contents_mother.get_class_file_contents()
    file = file_generator.invoke(class_file_contents)
    all_are_file = all([isinstance(file, File) for file in file])
    assert all_are_file
