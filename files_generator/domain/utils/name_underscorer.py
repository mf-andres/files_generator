import re


def underscore_name(name: str):
    uppercase_slices = re.findall('[A-Z][^A-Z]*', name)
    underscored_name = "_".join(uppercase_slices)
    return underscored_name
