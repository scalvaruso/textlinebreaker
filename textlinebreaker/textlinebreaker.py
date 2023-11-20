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

    # This check is to mantain the usability
    # of an external package (borders)
    # that relies on textlinebreaker.
    # This check will be removed in future versions
    if isinstance(line, list):
        words = line
    else:
        words = line.split(" ")
        
    # Check if the given max width is a valid number and lower than the terminal width
    if max_width > os.get_terminal_size().columns:
        max_width = os.get_terminal_size().columns
    elif max_width < 1:
        max_width = 1

    # Create a new list to store the new lines
    new_list = []
    new_line = ""
    space = " "
    
    # Adjust the alignment of the lines
    if alignment.lower() == "right":
        positioning = "{:>"
    elif alignment.lower()=="centre" or alignment.lower()=="center":
        positioning = "{:^"
    else:
        positioning = "{:<"
    adjustment = positioning + f"{max_width}" + "}"
    
    # Split the lines if they are longer than the max length characters.
    if words == [""]:
        new_list.append(" "*max_width)

    # Replace special character "\t"
    for word in words:
        word = word.replace("\t", "    ")
        
        if len(new_line+word) < (max_width+1):
            new_line += word + space

        else:
            if len(word) >= max_width:

                remaining_width = max_width - len(new_line)
                new_line += word[:remaining_width] + space
                word = word[remaining_width:]
                new_list.append(adjustment.format(new_line.rstrip(" ")))

                while len(word) >= max_width:
                    new_line = word[:max_width] + space
                    word = word[max_width:]
                    new_list.append(adjustment.format(new_line.rstrip(" ")))
                new_line = word + space

            else:
                new_list.append(adjustment.format(new_line.rstrip(" ")))
                new_line = word + space
    
    if new_line != " ":
        new_list.append(adjustment.format(new_line.rstrip(" ")))
        
    return new_list
