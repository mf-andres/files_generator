def read_class_file(class_file: str) -> str:
    with open(class_file, "r") as class_file:
        class_file_contents = class_file.read()
    return class_file_contents
