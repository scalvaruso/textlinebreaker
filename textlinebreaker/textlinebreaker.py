
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
import os  # Import the os module for accessing terminal size and other system-related functions

def _get_terminal_columns(default=80):
    try:
        return os.get_terminal_size().columns
    except OSError:
        return default


class TextLineBreaker:
    def __init__(self, text, max_width=_get_terminal_columns(), alignment="left"):
        self.text = text
        self.max_width = max_width
        self.alignment = alignment
        self.formatted_text = self.split_line()
    
    def split_line(self):
        words = self._valid_input(self.text)
        max_width = self._valid_width(self.max_width, words)
        new_list = []
        new_line = ""
        space = " "
    
        if self.alignment.lower() == "right":
            positioning = "{:>"
        elif self.alignment.lower() in ["centre", "center"]:
            positioning = "{:^"
        else:
            positioning = "{:<"
        
        adjustment = positioning + f"{max_width}" + "}"
        
        if words == [""]:
            new_list.append(" " * max_width)
        
        for word in words:
            word = word.replace("\t", "    ")

            if len(new_line + word) < (max_width + 1):
                new_line += word + space
            else:
                if len(word) > max_width:
                    remaining_width = max_width - len(new_line)
                    new_line += word[:remaining_width] + space
                    word = word[remaining_width:]
                    new_list.append(adjustment.format(new_line.rstrip(" ")))

                    while len(word) > max_width:
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

    def _valid_input(self, line):
        words = []
        if isinstance(line, list):
            for i in line:
                if isinstance(i, list):
                    words += i
                else:
                    words += i.split(" ")
        else:
            words = line.split(" ")
        return words
    
    def _valid_width(self, max_width, words):
        min_width = max(len(word) for word in words)
        if isinstance(max_width, int):
            if 9 <= max_width <= os.get_terminal_size().columns:
                pass
            elif max_width < min_width:
                max_width = min_width
            else:
                max_width = os.get_terminal_size().columns
        elif max_width.lower() == "min":
            max_width = min_width
        elif max_width.lower() == "2words":
            max_width = min_width + min(len(word) for word in words)
        else:
            max_width = os.get_terminal_size().columns
        return max_width
    
    def __str__(self):
        return "\n".join(self.formatted_text)


