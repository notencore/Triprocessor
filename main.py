#!/usr/bin/env/ python

import re
import sys

var_string = re.compile(r"^\$(.+):(.+)", re.M)
end_of_vars = re.compile("----")

def processString(string):
    #God I hate four tabs.
    groups = var_string.findall(string, 0, end_of_vars.search(string).start())
    for (key, value) in groups:
        print(key, value)
    return
with open(sys.argv[1]) as file:
    processString(file.read())