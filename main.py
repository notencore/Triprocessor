#!/usr/bin/env/ python

import re
import fileinput

comparison_string = re.compile(r"^\$(.+):(.+)", re.M)

def processString(string):
    #God I hate four tabs.
    groups = comparison_string.findall(string)
    for (key, value) in groups:
        print(key, value)
    return

processString("$Test:Works")