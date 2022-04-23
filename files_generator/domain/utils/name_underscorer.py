def underscore_name(name: str):
    uppercase_indexes = [index for index, char in enumerate(name) if char.isupper()]
    uppercase_indexes.pop(0)
    underscored_name = name
    for uppercase_index in uppercase_indexes:
        underscored_name = (
                underscored_name[:uppercase_index]
                + "_"
                + underscored_name[uppercase_index:]
        )
    return underscored_name
