import typer

from files_generator.application.converters_generator import FilesGenerator
from files_generator.infrastructure.class_file_reader import read_class_file
from files_generator.infrastructure.converters_writer import write_converters


def main(class_file: str, output_directory: str = "./converters"):
    class_file_contents = read_class_file(class_file)
    converters = FilesGenerator().invoke(class_file_contents)
    write_converters(converters, output_directory)


if __name__ == "__main__":
    typer.run(main)
