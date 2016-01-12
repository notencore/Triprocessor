class flags:
    BOLD = False
    ITALICS = False
    UNDERSCORE = False
    STRIKETHROUGH = False


def processMarkup(original_string):
    current_flags = flags()
    working_string = ""
    head = 0
    for num, character in enumerate(original_string):
        if  character == "*":
            if current_flags.BOLD:
                working_string = working_string[:num+head]+"[/b]"
                head += len("[/b]")
            else:
                working_string = working_string[:num+head]+"[b]"
                head += len("[b]")
            current_flags.BOLD = not current_flags.BOLD
            continue
        working_string += character
    return working_string