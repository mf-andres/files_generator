from typing import List

from files_generator.domain.file import File
from files_generator.domain.item_file_generator import ItemFileGenerator
from files_generator.domain.item_to_object_file_generator import ItemToObjectFileGenerator
from files_generator.domain.mongo_object_to_object_file_generator import MongoObjectToObjectFileGenerator
from files_generator.domain.object_to_item_file_generator import ObjectToItemFileGenerator
from files_generator.domain.object_to_mongo_object_file_generator import ObjectToMongoObjectFileGenerator


class FilesGenerator:
    def invoke(self, class_file_contents: str) -> List[File]:
        file_generators = [
            ItemToObjectFileGenerator(),
            ObjectToItemFileGenerator(),
            MongoObjectToObjectFileGenerator(),
            ObjectToMongoObjectFileGenerator(),
            ItemFileGenerator(),
        ]
        files = [
            file_generator.generate(class_file_contents) for file_generator in file_generators
        ]
        return files
