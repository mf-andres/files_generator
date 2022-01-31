import abc

from converters_generator.domain.converter import Converter


class ConverterGenerator(abc.ABC):
    @abc.abstractmethod
    def generate(self, class_file_contents: str) -> Converter:
        '''
        Initialize the converter.
        :return:
        '''
        pass

