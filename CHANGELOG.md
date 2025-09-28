# textlinebreaker

🆕 **v1.0.0 – Major Release**  
**Highlights:** Type hints, alignment options, borders, dynamic width, and doctest examples.

---

## v1.0.0 - 2025-09-28

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
- Border support via `delimiter(char)` method.
- Dynamic width support: "min", "2words", "max".
- Doctest examples included in the class docstring.

- **Added**
  - Edge case handling for empty input or single-word lines.
- **Changed**
  - Refactored `_break_lines` for clarity and improved input validation.

### v0.2.0 - 2024-04-20

- **Added**
  - New parameters (`"min"`, `"2words"`, `"max"`) to set different line widths.
- **Fixed**
  - Improved algorithm to better split the input in the desired length lines.

### v0.1.0 - 2023-11-20

- **Added**
  - Check for input type (string or list) to perform proper splitting.
- **Fixed**
  - Issue splitting string into single characters rather than words.
