class singleProcessor:
    
    def __init__(self, replaced_symbol, replacement_symbol, final = False):
        self.replaced_symbol = replaced_symbol
        self.replacement_symbol = replacement_symbol
        self.skip_flag = False
        self.final = final
    
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
                if not self.final:
                    self.skip_flag = True
                    print("Escaped:")
                    working_string+= character
                continue
            
            if character == self.replaced_symbol:
                working_string = working_string[:num+head]+self.replacement_symbol
                head += len(self.replacement_symbol)
            working_string += character
        return working_string