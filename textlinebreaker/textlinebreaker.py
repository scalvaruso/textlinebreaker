"""
Text Line Breaker is a Python utility class that splits text into
multiple lines of a specified maximum width.  

It supports alignment options and dynamic width calculation, making it useful 
for formatting and displaying text in terminal applications.

Parameters:
    text (str | list[str]): The input text, either as a single string or a list of strings.
    max_width (int | str | None): Maximum line width.  
        - Default: terminal width  
        - Allowed values:  
            int (≥ 9, ≤ terminal width)  
            "min"     → longest word length  
            "2words"  → longest + shortest word length  
            "max"     → terminal width  
    alignment (str): Alignment of text within the line.  
        - Default: "left"  
        - Allowed values: "left", "right", "center", "centre"
"""

import os
from typing import List, Union, Iterator, Optional


def _get_terminal_columns(default: int = 80) -> int:
    """
    Safely return the number of terminal columns.  
    Falls back to `default` if terminal size cannot be determined.
    """
    try:
        return os.get_terminal_size().columns
    except OSError:
        return default


class TextLineBreaker:
    """
    A class to break text into lines with custom width and alignment.

    Examples:
        >>> text = "Hello world from TextLineBreaker"
        >>> breaker = TextLineBreaker(text, max_width=12, alignment="left")
        >>> print(breaker)
        Hello world
        from
        TextLineBreaker

        >>> breaker_center = TextLineBreaker(text, max_width=20, alignment="center")
        >>> print(breaker_center.delimiter(char="|"))
        |  Hello world from   |
        |   TextLineBreaker   |
    """

    def __init__(self, text: Union[str, List[str]], max_width: Optional[Union[int, str]] = None, alignment: str = "left") -> None:
        self.raw_text: Union[str, List[str]] = text
        self.terminal_width: int = _get_terminal_columns()
        self.alignment: str = self._validate_alignment(alignment)
        self.text_blocks: List[List[str]] = self._validate_input(self.raw_text)
        self.max_width: int = self._validate_width(max_width)
        self.formatted_text: List[str] = self._break_lines()

    def _validate_input(self, input_text: Union[str, List[str]]) -> List[List[str]]:
        """
        Normalize input text into a list of word lists.  

        Example:  
            "Hello world" → [["Hello", "world"]]
        """
        if isinstance(input_text, str):
            input_text = [input_text]
        # Replace tabs with spaces and split into words
        return [str(item).replace("\t", "    ").split() for item in input_text]

    def _validate_alignment(self, alignment: str) -> str:
        """
        Ensure alignment is one of: left, right, or center.  
        Normalizes "centre" to "center".
        """
        alignment = alignment.lower()
        if alignment in ("center", "centre"):
            return "center"
        elif alignment == "right":
            return "right"
        return "left"

    def _validate_width(self, max_width: Optional[Union[int, str]]) -> int:
        """
        Determine the line width based on user input.  
        Handles integers, predefined keywords ("min", "2words"), or defaults.
        """
        # Flatten all words into a single list
        all_words = [word for line in self.text_blocks for word in line]
        # Longest word length ensures no truncation
        min_word_length = max((len(word) for word in all_words), default=10)

        if isinstance(max_width, int):
            # Clamp within valid range, respecting longest word length
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
        # Fallback to full terminal width
        return self.terminal_width

    def _get_alignment_format(self, width: Optional[int] = None) -> str:
        """
        Build a Python format string for the chosen alignment.  

        Example (center, width=10): "{:^10}"
        """
        align_map = {"left": "<", "center": "^", "right": ">"}
        if width is None:
            width = self.max_width
        return f"{{:{align_map[self.alignment]}{width}}}"

    def _break_lines(self, width: Optional[int] = None) -> List[str]:
        """
        Split input text into lines respecting max width and alignment.  

        Returns:
            list[str]: List of formatted lines.
        """
        all_lines: List[str] = []
        align_format: str = self._get_alignment_format(width)

        for word_list in self.text_blocks:
            current_line = ""
            for word in word_list:
                # Add word to current line if it fits, otherwise start new line
                if len(current_line + word) + (1 if current_line else 0) <= (width or self.max_width):
                    current_line += (word if not current_line else " " + word)
                else:
                    all_lines.append(align_format.format(current_line))
                    current_line = word
            if current_line:
                all_lines.append(align_format.format(current_line))

        # Ensure at least one blank line if no words
        if not all_lines:
            all_lines.append(" " * (width or self.max_width))

        return all_lines

    def delimiter(self, char: str = "|") -> str:
        """
        Return the formatted text surrounded by border characters.  

        Example (char="|"):  
            |Hello world   |
        """
        if not char:
            return "\n".join(self.formatted_text)

        inner_width: int = self.max_width - 2
        bordered_lines: List[str] = []
        for line in self._break_lines(inner_width):
            bordered_lines.append(f"{char}{line}{char}")
        return "\n".join(bordered_lines)

    def __str__(self) -> str:
        """Return the formatted text as a single string (joined by newlines)."""
        return "\n".join(self.formatted_text)

    def __iter__(self) -> Iterator[str]:
        """Allow iteration over formatted lines."""
        return iter(self.formatted_text)


# ---------------------------
# Example usage
# ---------------------------
if __name__ == "__main__":
    sample_text = "Text Line Breaker is a Python class that can split your text into multiple lines and align them neatly."
    
    print("=== Default (left-aligned) ===")
    breaker1 = TextLineBreaker(sample_text, max_width=30)
    print(breaker1)

    print("\n=== Center-aligned with border ===")
    breaker2 = TextLineBreaker(sample_text, max_width=30, alignment="center")
    print(breaker2.delimiter("~"))

    print("\n=== Right-aligned, width='2words' ===")
    breaker3 = TextLineBreaker(sample_text, max_width="2words", alignment="right")
    for line in breaker3:
        print(line)
