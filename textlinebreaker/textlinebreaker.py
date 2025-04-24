# ·········· ·········· ·········· textlinebreaker ·········· ·········· ·········· #
"""
Text Line Breaker is a Python script that takes a string or a list of strings, and breaks them into lines of a specified maximum width.
The functions 'format_lines' returns a list of tuples with the strings of the specified maximum width, text color, and backgroud color.
The function 'ttf' uses advanced formatting.
These functions can be particularly useful for formatting and displaying text in a terminal.

Parameters:
    line: is the main argument, it's the text that needs to be broken down
    max_width: allows to set the max length of text on a line.
        default value = terminal width
        allowed values: integers, "min", "2words", "max"
    alignment: allows to change the alignment of the text inside the frame.
        default value = "left"
        allowed values: "left", "centre", "center", "right"

NOTE: following parameters are for 'format_lines' and 'ttf' only
    color: allows to change the color of the text.
        default value = 37
        allowed values: most color names
                        RGB values [0-255];[0-255];[0-255]
                        Hex values #[00-FF][00-FF][00-FF]
                        xterm color number in the format x[0-255]
                        and ANSI codes 0, [30-37], [90-97]
    text_background: allows to change the background color of the text.
        default value = 0
        allowed values: most color names,
                        RGB values [0-255];[0-255];[0-255],
                        Hex values #[00-FF][00-FF][00-FF],
                        xterm color number in the format x[0-255],
                        and ANSI codes 0, [40-47], [100-107].

NOTE: following parameters are for 'ttf' only
    label_width:
        default value = 1
        allowed values: integers
    styling: 
        default value = True
        allowed values: True, 1, False, 0
"""

import os  # Import the os module for accessing terminal size and other system-related functions


def _get_terminal_columns(default=80):
    try:
        return os.get_terminal_size().columns
    except OSError:
        return default


# First importable function
def split_line(input_line, max_width=_get_terminal_columns(), alignment="left"):

    # _format_lines returns a list of formatted strings
    return _format_lines(input_line, max_width, alignment, styling=False)


def format_lines(input_line, max_width=_get_terminal_columns(), alignment="left", color=37, text_background=0):
    # _format_lines returns a list of tuples with formatted strings, Text Color, Background Color
    return _format_lines(input_line, max_width, alignment, color, text_background)


# ttf: Tagged Text Format
def ttf(input_line, max_width=_get_terminal_columns(), alignment="left", color=37, text_background=0, label_width=1, styling=True):
    # ttf returns a list of tuples with strings with advanced formatting, Text Color, Background Color
    # String formatting is as for the following example:
    """
    Text without a column is spread along all
    the available width of the line.
    Text with the column is aligned after the
    column.
    Heading 1 ··· :   This is the description
                      of the heading.
    Description · :   This is the explanation
                      of the second heading.
    Description 2 :   This is the explanation
                      of the third heading.
    """

    return _format_lines(input_line, max_width, alignment, color, text_background, label_width, styling)


def _format_lines(input_list, max_width, alignment, def_txt_col=37, def_txt_bg=0, label_width=0, styling=True):
    
    # Get a list of words from the input line
    """
    _valid_input returns a list of tuples with: TEXT, Alignement, Text Color, Background Color
    word[0] = TEXT
    word[1] = Alignement
    word[2] = Text Color
    word[3] = Background Color
    """
    words, header_length = _valid_input(input_list, alignment, def_txt_col, def_txt_bg, styling)
    # Validate and adjust the maximum width: at least one word, less than the terminal width.
    max_width = _valid_width(max_width, words)
    # Create a new list to store the new lines
    new_list = []  # Initialize an empty list to store lines
    new_line = ""  # Initialize an empty string to store the current line being constructed
    space = " "  # Initialize a variable for space character
    label_space = ""    # Initialize a variable for label space
    #header_length = 0
    
    # Split the lines if they are longer than the max length characters.
    if words == [""]:  # If there are no words
        new_list.append((" "*max_width), alignment, def_txt_col, def_txt_bg)  # Append an empty line with spaces
    
    for word in words:  # Iterate through each word
        """
        word[0] = TEXT
        word[1] = Alignement
        word[2] = Text Color
        word[3] = Background Color
        """
        string_word = word[0].replace("\t", "    ")  # Replace tab with four spaces

        tmp_line = new_line + string_word
        if label_width:
            if tmp_line[-1] == ":":
                header_length = max(len(tmp_line)-1,header_length)
                label_width = max(header_length+3,label_width)
        alignment = word[1]
        after_column = (label_width-(header_length+3)) // 4
        before_column = label_width - (after_column+3)

        if len(tmp_line) < (max_width+1):  # If adding the word does not exceed max width
            
            # Adding additional formatting for function "headings".

            if ":" in string_word and label_width: # "label_width" is differnt from 0 only when is called by the "headings" function
                # Removing eccessive spaces if heading word is longer than defined label width
                if len(tmp_line) > before_column:
                    ending = ""
                else:
                    ending = " "
                if word[1] == "left":
                    column_position = "{:·<" + f"{before_column}" + "}"
                    new_line = column_position.format(tmp_line.replace(":",ending)) + " : " + (space*after_column)
                else:
                    new_line += string_word
                label_space = space * (label_width)
            
            else:   # No additional formattings if no ":" is present or not called by "headings"
                new_line += string_word + space  # Add the word to the current line

        else:  # If adding the word exceeds max width
            if len(string_word) > max_width:  # If the word itself is longer than max width

                remaining_width = max_width - len(new_line)  # Calculate remaining space in the line
                new_line += string_word[:remaining_width] + space  # Add part of the word to the line
                word = string_word[remaining_width:]  # Update word to exclude the part added
                new_list.append(_append(word,max_width,new_line,styling))  # Append the line to new_list

                while len(string_word) > max_width:  # If the remaining part of the word is still longer than max width
                    new_line = label_space + string_word[:max_width] + space  # Add part of the word to the line
                    word = string_word[max_width:]  # Update word to exclude the part added
                    new_list.append(_append(word,max_width,new_line,styling))  # Append the line to new_list
                new_line = label_space + string_word + space  # Update new_line to contain the remaining part of the word

            else:  # If the word itself fits within the max width
                new_list.append(_append(word,max_width,new_line,styling))  # Append the current line to new_list
                new_line = label_space + string_word + space  # Start a new line with the current word
        
        if "\n" in new_line:
            new_line = new_line.replace("\n","")
            new_list.append(_append(word,max_width,new_line,styling))  # Append the current line to new_list
            new_line = ""
            label_space = ""
    
    if new_line != "":  # If there is content in the last line
        new_list.append(_append(word,max_width,new_line,styling))  # Append the last line to new_list

    # _format_lines returns a list of tuples with: TEXT, Text Color, Background Color
    return new_list  # Return the list of formatted lines


def _valid_input(line, alignment="left", def_col=37, def_txt_bg=0, styling=True):
    # This function validate the input
    # Convert input into a list of words
    words = []  # Initialize an empty list for words
    header_length = 0   # Setting header length to 0

    if isinstance(line, list):  # If input is already a list
        for i in line:  # Iterate through each item in the list

            if isinstance(i, list):  # If the item is also a list
                words_to_add, header_length = _valid_input(i, alignment, def_col, def_txt_bg, styling)
                words.append(words_to_add)  # Extend words list with the sublist
            """
            _get_settings returns a tuple with: TEXT, Alignement, Text Color, Background Color
            i[0] = TEXT
            i[1] = Alignement
            i[2] = Text Color
            i[3] = Background Color
            """
            i =  _get_settings(i, def_col, def_txt_bg, alignment, styling)

            if i[0] == "":
                new_i = i[0] + "\n"
                """
                elif len(i[0].split(" ")) == 1: # and "..." in i:
                    new_i = i[0]
                """
            else:
                new_i = i[0] + "\n"
            #elif i[-1] == ".":
                #   i += "\n"
            items = new_i.split(" ")  # Split the item by spaces and extend words list
            for word in items:
                if ":" in word:
                    header_length = max(len(word)-1,header_length)
                words.append(_append_input(word,i,styling))

    else:  # If input is not a list
        i =  _get_settings(line, def_col, def_txt_bg, alignment, styling)

        if i[0] == "":
            new_i = i[0] + "\n"
        elif len(i[0].split(" ")) == 1: # and "..." in i:
            new_i = i[0]
        else:
            new_i = i[0] + "\n"
        #elif i[-1] == ".":
            #   i += "\n"
        items = new_i.split(" ")  # Split the item by spaces and extend words list
        for word in items:
            if ":" in word:
                header_length = max(len(word)-1,header_length)
            words.append(_append_input(word,i,styling))

    # _valid_input returns a tuple with: TEXT, Alignement, Text Color, Background Color
    return words, header_length  # Return the list of words


def _valid_width(max_width, words):
    # Check if the given max width is a valid number
    # and lower than the terminal width

    min_width = max(len(word) for word in words)  # Get the maximum word length
    
    if isinstance(max_width, int):  # If max_width is an integer

        if 9 <= max_width <= _get_terminal_columns():  # If max_width is within valid range.
            pass  # Do nothing
        elif max_width < min_width:  # If max_width is less than the minimum word length
            max_width = min_width  # Set max_width to the minimum word length
        else:  # If max_width exceeds terminal width
            max_width = os.get_terminal_size().columns  # Set max_width to terminal width

    elif max_width.lower()=="min":  # If max_width is set to "min"
        max_width = min_width  # Set max_width to the minimum word length
    elif max_width.lower()=="2words":  # If max_width is set to "2words"
        max_width = min_width + min(len(word) for word in words)  # Set max_width to the sum of two minimum word lengths
    else:  # If max_width is not an integer or a recognized keyword
        max_width = os.get_terminal_size().columns  # Set max_width to terminal width
    
    return max_width  # Return the validated max width


# This function returns a tuple with: TEXT, Alignement, Text Color, Background Color.
def _get_settings(item, color, text_background, alignment, styling):

    # Check if item is a tuple, and get values for foreground, background colors, and alignment (t_color, t_background, line_alignment).
    if isinstance(item, tuple):
        parameters = len(item)
        
        """
        If True:
        item[0] is the string.
        item[1] can be the color of the text or line alignment.
        item[2] is optional and could be the backgroud color or line alignment.
        item[3] is optional and is the line alignment.
        """

        s_text = item[0]

        if parameters == 2:
            # Check if first item after string is the text color or the alignment.
            if str(item[1]).lower() in ("left","center","centre","right"):
                line_alignment = item[1]
                t_color = color
            else:
                if item[1] != "":
                    t_color = item[1]
                else:
                    t_color = color
                line_alignment = alignment
            t_background = text_background

        elif parameters == 3:
            # Get text color from item[1].
            if item[1] != "":
                t_color = item[1]
            else:
                t_color = color
            # Check if second item after string is the background color or the alignment.
            if str(item[2]).lower() in ("left","center","centre","right"):
                line_alignment = item[2]
                t_background = text_background
            else:
                if item[2] != "":
                    t_background = item[2]
                else:
                    t_background = text_background
                line_alignment = alignment

        else:
            # Get text color from item[1].
            if item[1] != "":
                t_color = item[1]
            else:
                t_color = color
            # Get background color from item[2].
            if item[2] != "":
                t_background = item[2]
            else:
                t_background = text_background
            # Get alignment from item[3].
            if str(item[3]).lower() in ("left","center","centre","right"):
                line_alignment = item[3]
            else:
                line_alignment = alignment
        
    # If item is not a tuple, default colors are assigned to the lines.
    else:
        s_text = item
        t_color = color
        t_background = text_background
        line_alignment = alignment

    if styling:
        # _get_settings returns a tuple with: TEXT, Alignement, Text Color, Background Color
        return (s_text, line_alignment, t_color, t_background)
    else:
        return (s_text, line_alignment)


def _adjustment(alignment,max_width):
    if alignment.lower() == "right":  # Right alignment
        positioning = "{:>"  # Format specifier for right alignment
    elif alignment.lower()=="centre" or alignment.lower()=="center":  # Center alignment
        positioning = "{:^"  # Format specifier for center alignment
    else:  # Left alignment (default)
        positioning = "{:<"  # Format specifier for left alignment

    return positioning + f"{max_width}" + "}"  # Adjustment string for styling


def _append(word,max_width,new_line,styling):
    if styling:
        return (_adjustment(word[1],max_width).format(new_line.rstrip(" ")),word[2],word[3])
    else:
        return _adjustment(word[1],max_width).format(new_line.rstrip(" "))
    

def _append_input(word,i,styling):
    if styling:
        return (word,i[1],i[2],i[3])
    else:
        return (word,i[1])
