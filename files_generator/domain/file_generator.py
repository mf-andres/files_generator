import abc

from files_generator.domain.file import File


class FileGenerator(abc.ABC):
    @abc.abstractmethod
    def generate(self, class_file_contents: str) -> File:
        '''
        Initialize the file.
        :return:
        '''
        pass

