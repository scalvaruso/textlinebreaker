from .textlinebreaker import *

# -----------------------------
# Public API
# -----------------------------
__all__ = ["TextLineBreaker"]

# -----------------------------
# Deprecated old function
# -----------------------------
def split_line(*args, **kwargs):
    """
    The `split_line()` function is removed in v1.0.0.
    You must update your code to use `TextLineBreaker`.

    Example migration:

    Old usage:
        lines = split_line(text, max_width=30, alignment="center")

    New usage:
        breaker = TextLineBreaker(text, max_width=30, alignment="center")
    """
    raise RuntimeError(
        "\n\n\033[41m`split_line()` is no longer supported in v1.0.0.\033[0m\n"
        "\n\033[33mPlease update your code to use the \033[92m`TextLineBreaker` class.\033[0m\n\n"
        "Example migration:\n"
        "  breaker = TextLineBreaker(text, max_width=30, alignment='center')\n\n"
        "Visit:\n"
        "  https://github.com/scalvaruso/textlinebreaker/blob/main/README.md\n"
    )
