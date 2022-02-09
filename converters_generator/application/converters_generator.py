from typing import List

from converters_generator.domain.converter import Converter
from converters_generator.domain.item_to_object_converter_generator import ItemToObjectConverterGenerator
from converters_generator.domain.mongo_object_to_object_converter_generator import MongoObjectToObjectConverterGenerator
from converters_generator.domain.object_to_item_converter_generator import ObjectToItemConverterGenerator
from converters_generator.domain.object_to_mongo_object_converter_generator import ObjectToMongoObjectConverterGenerator


class ConvertersGenerator:
    def invoke(self, class_file_contents: str) -> List[Converter]:
        converter_generators = [
            ItemToObjectConverterGenerator(),
            ObjectToItemConverterGenerator(),
            MongoObjectToObjectConverterGenerator(),
            ObjectToMongoObjectConverterGenerator(),
        ]
        generators = [
            converter_generator.generate(class_file_contents) for converter_generator in converter_generators
        ]
        return generators
