import os  # Import the os module for accessing terminal size and other system-related functions

def split_line(line, max_width=os.get_terminal_size().columns, alignment="left"):
    """
    Text Line Breaker is a Python script that takes a list of text items,
    breaks them into lines of a specified maximum width.
    This can be particularly useful for formatting and displaying text in a terminal.

    Parameters:
        line: is the main argument, it's the text that needs to be broken down
        max_width: allows to set the max length of text on a line.
            default value = terminal width
            allowed values: integers, "min", "2words", "max"
        alignment: allows to change the alignment of the text inside the frame.
            default value = "left"
            allowed values: "left", "centre", "center", "right"
    """
    
    # Get a list of words from the input line
    words = _valid_input(line)
    
    # Validate and adjust the maximum width: at least one word, less than the terminal width.
    max_width = _valid_width(max_width, words)
    
    # Create a new list to store the new lines
    new_list = []  # Initialize an empty list to store lines
    new_line = ""  # Initialize an empty string to store the current line being constructed
    space = " "  # Initialize a variable for space character
    
    # Adjust the alignment of the lines based on the specified alignment
    if alignment.lower() == "right":  # Right alignment
        positioning = "{:>"  # Format specifier for right alignment
    elif alignment.lower()=="centre" or alignment.lower()=="center":  # Center alignment
        positioning = "{:^"  # Format specifier for center alignment
    else:  # Left alignment (default)
        positioning = "{:<"  # Format specifier for left alignment
    adjustment = positioning + f"{max_width}" + "}"  # Adjustment string for formatting
    
    # Split the lines if they are longer than the max length characters.
    if words == [""]:  # If there are no words
        new_list.append(" "*max_width)  # Append an empty line with spaces
    
    for word in words:  # Iterate through each word
        word = word.replace("\t", "    ")  # Replace tab with four spaces

        if len(new_line+word) < (max_width+1):  # If adding the word does not exceed max width
            new_line += word + space  # Add the word to the current line

        else:  # If adding the word exceeds max width
            if len(word) > max_width:  # If the word itself is longer than max width

                remaining_width = max_width - len(new_line)  # Calculate remaining space in the line
                new_line += word[:remaining_width] + space  # Add part of the word to the line
                word = word[remaining_width:]  # Update word to exclude the part added
                new_list.append(adjustment.format(new_line.rstrip(" ")))  # Append the line to new_list

                while len(word) > max_width:  # If the remaining part of the word is still longer than max width
                    new_line = word[:max_width] + space  # Add part of the word to the line
                    word = word[max_width:]  # Update word to exclude the part added
                    new_list.append(adjustment.format(new_line.rstrip(" ")))  # Append the line to new_list
                new_line = word + space  # Update new_line to contain the remaining part of the word

            else:  # If the word itself fits within the max width
                new_list.append(adjustment.format(new_line.rstrip(" ")))  # Append the current line to new_list
                new_line = word + space  # Start a new line with the current word
    
    if new_line != " ":  # If there is content in the last line
        new_list.append(adjustment.format(new_line.rstrip(" ")))  # Append the last line to new_list
    
    return new_list  # Return the list of formatted lines


def _valid_input(line):
    # This function validate the input and width
    # Convert input into a list of words

    words = []  # Initialize an empty list for words

    if isinstance(line, list):  # If input is already a list
        for i in line:  # Iterate through each item in the list
            if isinstance(i, list):  # If the item is also a list
                words += i  # Extend words list with the sublist
            else:  # If the item is not a list
                words += i.split(" ")  # Split the item by spaces and extend words list
    else:  # If input is not a list
        words = line.split(" ")  # Split the line by spaces
    
    return words  # Return the list of words


def _valid_width(max_width, words):
    # Check if the given max width is a valid number
    # and lower than the terminal width

    min_width = max(len(word) for word in words)  # Get the maximum word length
    
    if isinstance(max_width, int):  # If max_width is an integer

        if 9 <= max_width <= os.get_terminal_size().columns:  # If max_width is within valid range.
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
