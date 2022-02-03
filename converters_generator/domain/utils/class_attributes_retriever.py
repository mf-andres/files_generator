from converters_generator.domain.utils.word_end_index_retriever import get_word_end_index


def get_class_attributes(class_file_contents: str):
    self_end_index = get_word_end_index(class_file_contents, "self,")
    first_attribute_line_index = len(class_file_contents[:self_end_index]) + class_file_contents[self_end_index:].find(
        "\n") + 1
    end_of_init_function_index = class_file_contents.find("):")
    last_attribute_line_end_index = class_file_contents[:end_of_init_function_index].rfind("\n")
    attributes_definition = class_file_contents[first_attribute_line_index: last_attribute_line_end_index]
    attribute_names = []
    for line in attributes_definition.splitlines():
        colon_index = line.find(":")
        attribute_name = line[:colon_index].strip()
        attribute_names.append(attribute_name)
        comma_index = line.find(",")
        attribute_type = line[colon_index:comma_index].strip()
    return attribute_names

