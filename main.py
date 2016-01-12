#!/usr/bin/env/ python

#Standard Modules#
import re
import sys

#Function Definitions#
from substituteStrings import substituteStrings
from processMarkup import processMarkup

def processString(original_string):
    working_string = substituteStrings(original_string)
    working_string = processMarkup(working_string)
    print(working_string)
    return

with open(sys.argv[1]) as file:
    processString(file.read())
