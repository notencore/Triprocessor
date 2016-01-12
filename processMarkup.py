from pairProcessor import pairProcessor
from singleProcessor import singleProcessor

processorList = [\
    pairProcessor("*","[b]","[/b]"),   \
    pairProcessor("-", "[i]", "[/i]"), \
    pairProcessor("_", "[u]", "[/u]"), \
    pairProcessor("~", "[s]", "[/s]"), \
    singleProcessor("\\", "", True)    \
]

def processMarkup(original_string):
    working_string = original_string
    for processor in processorList:
        working_string = processor.processMarkup(working_string)
    return working_string
    