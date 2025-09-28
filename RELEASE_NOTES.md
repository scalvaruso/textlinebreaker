# textlinebreaker

🆕 **v1.0.0 – Major Release**  
**Highlights:** Type hints, alignment options, borders, dynamic width, and doctest examples.

---

## Release Notes

### Version 1.0.0

**Upgrade Notes:**  
Users can now take advantage of type hints, text alignment, borders, dynamic width options, and doctest examples.

**Migration / Upgrade Tips:**

- `TextLineBreaker` now uses type hints; adjust IDE/type-checking if needed.
- Alignment can be specified using `"left"`, `"center"`/`"centre"`, or `"right"`.
- Use `delimiter(char)` to wrap text lines in borders.
- Width can now be set dynamically with `"min"`, `"2words"`, or `"max"`.
- Doctest examples are included for automated testing or reference.

**Highlights:**

- Type hints for all methods and constructor.
- Alignment options: "left", "center"/"centre", "right".
- Border functionality via `delimiter(char)` method.
- Dynamic width support: "min", "2words", "max".
- Doctest examples included in class docstring.

- Added edge case handling for empty input or single-word lines.
- Refactored `_break_lines` and improved input validation.

#### Version 0.2.0

- Added new parameters (`"min"`, `"2words"`, `"max"`) to set different line widths.
- Improved algorithm to better split the input in the desired length lines.

#### Version 0.1.0

- Fixed a bug where the string was split in single characters rather than words.
- Added a check for input type (string or list) to ensure correct splitting.
