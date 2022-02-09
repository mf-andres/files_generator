import typer

from files_generator.application.files_generator import FilesGenerator
from files_generator.infrastructure.class_file_reader import read_class_file
from files_generator.infrastructure.files_writer import write_files


def main(class_file: str, output_directory: str = "./files"):
    class_file_contents = read_class_file(class_file)
    file = FilesGenerator().invoke(class_file_contents)
    write_files(file, output_directory)


if __name__ == "__main__":
    typer.run(main)
