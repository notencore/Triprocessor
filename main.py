#!/usr/bin/env/ python

import re
import sys

text_sub_regex = re.compile(r"^(\$.+):(.+)", re.M)
header_end_regex = re.compile("----")

def processString(working_string):
    header_end_position = header_end_regex.search(working_string).end()
    text_sub_groups = text_sub_regex.findall(working_string, 0, header_end_position)
    working_string = working_string[header_end_position:]
    for (key, value) in text_sub_groups:
        working_string = working_string.replace(key, value)
    #for num, character in enumerate(working_string):
    #    if  character == "*":
    #        working_string = working_string[:num]+"[b]"+working_string[num+1:]
    print(working_string)
    return

with open(sys.argv[1]) as file:
    processString(file.read())
