class pairProcessor:
    
    def __init__(self, replaced_symbol, replacement_symbol_on, replacement_symbol_off):
        self.replaced_symbol = replaced_symbol #The symbol to be replaced, e.g. *
        self.replacement_symbol_on = replacement_symbol_on #The symbol when turning on, e.g. [b]
        self.replacement_symbol_off = replacement_symbol_off #The symbol when turning off, e.g. [/b]
        self.active_flag = False
        self.skip_flag = False
    
    def processMarkup(self, original_string):
        print(self.replaced_symbol)
        working_string = ""
        head = 0
        for num, character in enumerate(original_string):
            if self.skip_flag: #Check if we're escaped.
                working_string += character #Print without parsing.
                self.skip_flag = False
                print(num, character)
                continue
        
            if character == "\\": #Check for the escape character.
                self.skip_flag = True
                print("Escaped:")
                working_string+= character
                continue
            
            if character == self.replaced_symbol:
                if self.active_flag:
                    print(num)
                    working_string = working_string[:num+head]+self.replacement_symbol_off
                    head += len(self.replacement_symbol_off)
                else:
                    working_string = working_string[:num+head]+self.replacement_symbol_on
                    head += len(self.replacement_symbol_on)
                self.active_flag = not self.active_flag
                continue
            working_string += character
        return working_string