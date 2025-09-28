# Textlinebreaker

[![Static Badge](https://img.shields.io/badge/textlinebreaker-py-blue%3Fstyle%3Dflat%26logo%3Dpython%26logoWidth%3D20.svg?logo=python&color=blue)](https://github.com/scalvaruso/textlinebreaker/)
[![PyPI - Version](https://img.shields.io/pypi/v/textlinebreaker?logo=pypi&logoColor=white&color=blue)](https://pypi.org/project/textlinebreaker/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/textlinebreaker?logo=python)](https://pypi.org/project/textlinebreaker/)
[![Downloads](https://static.pepy.tech/badge/textlinebreaker)](https://pepy.tech/project/textlinebreaker)
[![PyPI - License](https://img.shields.io/pypi/l/textlinebreaker?color=blue)](https://github.com/scalvaruso/textlinebreaker/blob/main/LICENSE.md)

<!---
[![PyPI - status](https://img.shields.io/pypi/status/:textlinebreaker)](https://pypi.org/project/textlinebreaker/)
[![Documentation Status](https://readthedocs.org/projects/textlinebreaker/badge/?version=latest)](https://textlinebreaker.readthedocs.io/en/latest/?badge=latest)
-->

## Description

Text Line Breaker is a Python utility class that splits text into multiple lines of a specified maximum width.  
It supports alignment options and dynamic width calculation, making it useful for formatting and displaying text in terminal applications.

## Features

- Break text into multiple lines with a configurable maximum width.  
- Alignment options: **left, center, right**.  
- Dynamic width selection (`"min"`, `"2words"`, `"max"`, or integer values).  
- Supports input as **string** or **list of strings**.  
- Class-based design with built-in string conversion, iteration, and border formatting.  

## Latest Version 1.0.0

- **New class-based API**: `TextLineBreaker` replaces the old `split_line` function.  
- Added methods:
  - `__str__()` → return formatted text as string  
  - `__iter__()` → iterate through formatted lines  
  - `.delimiter(char="|")` → wrap lines with border characters  
- Improved input handling (lists, tabs, fallback terminal width).  
- Alignment normalized: `"centre"` maps to `"center"`.  
- Safer and more flexible width validation.  

⚠️ **Breaking change**:  
The old function `split_line()` is no longer the main entry point.  
Use the `TextLineBreaker` class instead.  

## Table of Contents

- [Getting Started](#getting-started)  
  - [Prerequisites](#prerequisites)  
  - [Installation](#installation)  
- [Usage](#usage)  
  - [Parameters](#parameters)  
  - [Examples](#examples)  
- [Migration from 0.2.0](#migration-from-020)  
- [Contributing](#contributing)  
- [License](#license)  

## Getting Started

### Prerequisites

This package relies only on the Python standard library and does not require additional dependencies.

### Installation

- Install the package with pip:

```bash
pip install textlinebreaker
````

- Or upgrade it:

```bash
pip install --upgrade textlinebreaker
```

- Import the class in your program:

```python
from textlinebreaker import TextLineBreaker
```

## Usage

The `TextLineBreaker` class takes a string or list of strings and breaks it into lines according to the specified maximum width and alignment.
The default width is the terminal width.

### Parameters

The `TextLineBreaker` class accepts the following parameters:

- **`text`**: the input text.

  - allowed values: `str`, `list[str]`
- **`max_width`**: maximum width for each line.

  - allowed values: integer (≥ 9, ≤ terminal width), `"min"`, `"2words"`, `"max"`
  - default: terminal width
- **`alignment`**: text alignment inside the line.

  - allowed values: `"left"`, `"right"`, `"center"`, `"centre"`
  - default: `"left"`

### Examples

```python
from textlinebreaker import TextLineBreaker

text = "Text Line Breaker is a Python class that can split your text into multiple lines and align them neatly."

# Example 1: Left alignment, fixed width
breaker1 = TextLineBreaker(text, max_width=30)
print(breaker1)

# Example 2: Center alignment with borders
breaker2 = TextLineBreaker(text, max_width=30, alignment="center")
print(breaker2.delimiter(char="|"))

# Example 3: Right alignment, width="2words"
breaker3 = TextLineBreaker(text, max_width="2words", alignment="right")
for line in breaker3:
    print(line)
```

Example output:

```bash
=== Left aligned ===
Text Line Breaker is a Python 
class that can split your text
into multiple lines and align 
them neatly.

=== Center aligned with borders ===
|   Text Line Breaker is a   |
|Python class that can split |
|  your text into multiple   |
|lines and align them neatly.|

=== Right aligned ===
Text Line
  Breaker
     is a
   Python
    class
 that can
    split
your text
     into
 multiple
lines and
    align
     them
  neatly.
```

## Migration from 0.2.0

In **v0.2.0**, you used a function:

```python
from textlinebreaker import split_line

text = "Hello world"
lines = split_line(text, max_width=20, alignment="center")

for line in lines:
    print(line)
```

In **v1.0.0**, use the class instead:

```python
from textlinebreaker import TextLineBreaker

text = "Hello world"
breaker = TextLineBreaker(text, max_width=20, alignment="center")

for line in breaker:
    print(line)
```

Key differences:

- `split_line()` → replaced by `TextLineBreaker` class.
- Iterating works directly on the class (`for line in breaker`).
- `print(breaker)` prints the whole formatted block.
- `.delimiter("|")` adds borders around the text.

---

## Contributing

If you'd like to contribute to this project, please follow these steps:

1. Fork the repository on GitHub.
2. Clone the fork to your local machine.
3. Create a new branch for your feature or bug fix.
4. Make your changes and commit them.
5. Push the changes to your fork on GitHub.
6. Create a pull request to the original repository.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/scalvaruso/textlinebreaker/blob/main/LICENSE.md) file for details.
