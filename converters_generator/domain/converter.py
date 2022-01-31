import abc


class Converter(abc.ABC):
    @abc.abstractmethod
    def file_name(self) -> str:
        '''
        Retrieve the converter file name.
        :return:
        '''
        pass

    @abc.abstractmethod
    def file_contents(self) -> str:
        '''
        Retrieve the converter file contents.
        :return:
        '''
        pass
