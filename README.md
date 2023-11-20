# Textlinebreaker

[<img src="https://img.shields.io/badge/textlinebreaker-py-blue?style=flat&logo=python&logoWidth=20.svg/"></a>](https://github.com/scalvaruso/textlinebreaker/)
[![PyPI - Version](https://img.shields.io/pypi/v/textlinebreaker?logo=pypi&logoColor=white&color=blue)](https://pypi.org/project/textlinebreaker/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/textlinebreaker?logo=python)](https://pypi.org/project/textlinebreaker/)
[![Downloads](https://static.pepy.tech/badge/textlinebreaker)](https://pepy.tech/project/textlinebreaker)
[![PyPI - License](https://img.shields.io/pypi/l/textlinebreaker?color=blue)](https://github.com/scalvaruso/textlinebreaker/blob/main/LICENSE.md)

<!---
[![PyPI - status](https://img.shields.io/pypi/status/:textlinebreaker)](https://pypi.org/project/textlinebreaker/)
[![Documentation Status](https://readthedocs.org/projects/textlinebreaker/badge/?version=latest)](https://textlinebreaker.readthedocs.io/en/latest/?badge=latest)
-->

## Description

Text Line Breaker is a Python script that takes a string of text and breaks it into lines of a specified maximum width. This tool is particularly useful for formatting and displaying text in a terminal.

## Features

- Split text lines to fit within a specified maximum width.
- Choose alignment options for the text (left, center, right).
- Adjust the maximum width (default value is the terminal width).

## Latest Version 0.1.0

- Fixed a bug where the string was split in single characters rather than in words.
- Added a check for the input to establish if it is a list or a string in order to perform the correct splitting method.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Parameters](#parameters)
  - [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites

This script relies on the Python standard library and does not require any additional dependencies.

### Installation

- Install the package with pip

```bash
  pip install textlinebreaker
```

- Import the package in your program

```python
  from textlinebreaker import split_line
```

## Usage

This function takes a long string of text as input and breaks it into lines according to the specified maximum width.
The default length is the width of the terminal.

### Parameters

The `split_line` function accepts the following parameters:

- `line`: is the main argument, it's the text that needs to be broken down.
- `max_width`: Allows you to set the maximum length of text on a line. Default value is the terminal width. Allowed values are integers.
- `alignment`: Allows you to change the alignment of the text inside the frame. Default value is "left". Allowed values are "left", "centre" or "center", and "right".

### Examples

Here's an example of how to use the `split_line` function:

```python
from textlinebreaker import split_line

text = "This is an example of text line breaking using the Text Line Breaker script."
lines = split_line(text, max_width=30, alignment="center")

for line in lines:
  print(line)
```

Output:

```bash
 This is an example of text 
line breaking using the Text 
    Line Breaker script.     
```

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
