from converters_generator.domain.utils.word_end_index_retriever import get_word_end_index


def get_class_name(class_file_contents: str) -> str:
    class_name_position = get_word_end_index(class_file_contents, "class") + 1
    colon_position = class_file_contents.find(":")
    class_name = class_file_contents[class_name_position + 1: colon_position]
    return class_name
