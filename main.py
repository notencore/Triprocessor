#!/usr/bin/env/ python

import re
import sys

var_string = re.compile(r"^(\$.+):(.+)", re.M)
end_of_vars = re.compile("----")

def processString(string):
    last_var_pos = end_of_vars.search(string).end()
    groups = var_string.findall(string, 0, last_var_pos)
    string = string[last_var_pos:]
    for (key, value) in groups:
        string = string.replace(key, value)
    print(string)
    return

with open(sys.argv[1]) as file:
    processString(file.read())
