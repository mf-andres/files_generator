from typing import List

from converters_generator.domain.converter import Converter


class ConvertersGenerator:
    def invoke(self, class_file_contents: str) -> List[Converter]:
        class FakeConverter(Converter):
            def file_name(self) -> str:
                return "file_name"
            def file_contents(self) -> str:
                return "file_contents"
        converters = [FakeConverter(), FakeConverter(), FakeConverter(), FakeConverter()]
        return converters
