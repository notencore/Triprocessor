class markupProcessor:
    
    def __init__(self, replaced_symbol, replacement_symbol_on, replacement_symbol_off):
        self.replaced_symbol = replaced_symbol #The symbol to be replaced, e.g. *
        self.replacement_symbol_on = replacement_symbol_on #The symbol when turning on, e.g. [b]
        self.replacement_symbol_off = replacement_symbol_off #The symbol when turning off, e.g. [/b]
        self.active_flag = False
    
    def processMarkup(self, original_string):
        working_string = ""
        head = 0
        for num, character in enumerate(original_string):
            if character == self.replaced_symbol:
                if self.active_flag:
                    working_string = working_string[:num+head]+self.replacement_symbol_off
                    head += len(self.replacement_symbol_off)
                else:
                    working_string = working_string[:num+head]+self.replacement_symbol_on
                    head += len(self.replacement_symbol_on)
                self.active_flag = not self.active_flag
                continue
            working_string += character
        return working_string

processorList = [\
    markupProcessor("*","[b]","[/b]"),  \
    markupProcessor("-", "[i]", "[/i]"),\
    markupProcessor("_", "[u]", "[/u]") \
]

def processMarkup(original_string):
    working_string = original_string
    for processor in processorList:
        working_string = processor.processMarkup(working_string)
    return working_string
    