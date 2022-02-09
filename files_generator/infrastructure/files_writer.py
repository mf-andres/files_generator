import os.path
from typing import List
from files_generator.domain.file import File


def write_converters(converters: List[File], output_directory: str):
    if not os.path.exists(output_directory):
        os.mkdir(output_directory)
    if not os.path.isdir(output_directory):
        raise Exception("Given path is not a directory")
    [write_converter(converter, output_directory) for converter in converters]


def write_converter(converter: File, output_directory: str):
    converter_file_name = output_directory + "/" + converter.file_name
    with open(converter_file_name, "w") as converter_file:
        converter_file.write(converter.file_contents)
