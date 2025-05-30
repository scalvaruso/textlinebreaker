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
    def __init__(self, text, max_width=None, alignment="left"):
        self.raw_text = text
        self.terminal_width = _get_terminal_columns()
        self.alignment = self._validate_alignment(alignment)
        self.text_blocks = self._validate_input(self.raw_text)
        self.max_width = self._validate_width(max_width)
        self.formatted_text = self._break_lines()

    def _validate_input(self, input_text):
        """Ensure input is a list of strings, split into words per string."""
        if isinstance(input_text, str):
            input_text = [input_text]
        return [str(item).replace("\t", "    ").split() for item in input_text]

    def _validate_alignment(self, alignment):
        alignment = alignment.lower()
        if alignment in ("center", "centre"):
            return "center"
        elif alignment == "right":
            return "right"
        return "left"

    def _validate_width(self, max_width):
        all_words = [word for line in self.text_blocks for word in line]
        min_word_length = max((len(word) for word in all_words), default=10)

        if isinstance(max_width, int):
            if 9 <= max_width <= self.terminal_width:
                return max(max_width, min_word_length)
            return min_word_length
        elif isinstance(max_width, str):
            max_width = max_width.lower()
            if max_width == "min":
                return min_word_length
            elif max_width == "2words":
                shortest = min((len(w) for w in all_words), default=1)
                return min_word_length + shortest
        return self.terminal_width

    def _get_alignment_format(self):
        align_map = {"left": "<", "center": "^", "right": ">"}
        return f"{{:{align_map[self.alignment]}{self.max_width}}}"

    def _break_lines(self):
        """Split each sentence into lines and align them."""
        align_format = self._get_alignment_format()
        all_lines = []

        for word_list in self.text_blocks:
            current_line = ""
            for word in word_list:
                if len(current_line + word) + (1 if current_line else 0) <= self.max_width:
                    current_line += (word if not current_line else " " + word)
                else:
                    all_lines.append(align_format.format(current_line))
                    current_line = word
            if current_line:
                all_lines.append(align_format.format(current_line))
        if not all_lines:
            all_lines.append(" " * self.max_width)
        return all_lines

    def __str__(self):
        return "\n".join(self.formatted_text)
    
    def __iter__(self):
        return iter(self.formatted_text)
