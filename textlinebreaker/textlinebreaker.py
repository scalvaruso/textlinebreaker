import os


def split_line(line, max_width=os.get_terminal_size().columns, alignment="left"):
    
    """
    Text Line Breaker is a Python script that takes a list of text items,
    breaks them into lines of a specified maximum width.
    This can be particularly useful for formatting and displaying text in a terminal.

    Parameters:
        line: is the main argument, it's the text that needs to be broken down
        max_width: allows to set the max length of text on a line.
            default value = terminal width
            allowed values: integers
        alignment: allows to change the alignment of the text inside the frame.
            default value = "left"
            allowed values: "left", "centre", "center", "right"
    """

    if max_width > os.get_terminal_size().columns:
        max_width = os.get_terminal_size().columns
    elif max_width < 1:
        max_width = 1

    new_list = []
    new_line = ""
    space = " "
    #adjustment = "{:^50}"
    if alignment.lower() == "right":
        positioning = "{:>"
    elif alignment.lower()=="centre" or alignment.lower()=="center":
        positioning = "{:^"
    else:
        positioning = "{:<"
    adjustment = positioning + f"{max_width}" + "}"
    
    # Split the lines if they are longer than the max length characters.
    
    if line == [""]:
        new_list.append(" "*max_width)

    for word in line:
        word = word.replace("\t", "    ")
        
        if len(new_line+word) < (max_width+1):
            new_line += word + space

        else:
            if len(word) >= max_width:

                remaining_width = max_width - len(new_line)
                new_line += word[:remaining_width] + space
                word = word[remaining_width:]
                #new_line = adjustment.format(new_line.rstrip(" "))    #Test alignement
                new_list.append(adjustment.format(new_line.rstrip(" ")))

                while len(word) >= max_width:
                    new_line = word[:max_width] + space
                    word = word[max_width:]
                    #new_line = adjustment.format(new_line.rstrip(" "))    #Test alignement
                    new_list.append(adjustment.format(new_line.rstrip(" ")))
                new_line = word + space

            else:
                #new_line = adjustment.format(new_line.rstrip(" "))    #Test alignement
                new_list.append(adjustment.format(new_line.rstrip(" ")))
                new_line = word + space
    
    if new_line != " ":
        #new_line = adjustment.format(new_line.rstrip(" "))    #Test alignement
        new_list.append(adjustment.format(new_line.rstrip(" ")))
        
    return new_list