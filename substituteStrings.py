import re

text_sub_regex = re.compile(r"^(\$.+):(.+)", re.M)
header_end_regex = re.compile("----")

def substituteStrings(working_string):
    header_end_position = header_end_regex.search(working_string).end()
    text_sub_groups = text_sub_regex.findall(working_string, 0, header_end_position)
    working_string = working_string[header_end_position+1:]
    for (key, value) in text_sub_groups:
        working_string = working_string.replace(key, value)
    return working_string