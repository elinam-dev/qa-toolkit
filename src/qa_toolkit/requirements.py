from typing import Any, Callable


def check_requirements(
    value: Any, rules: dict[str, Callable[[Any], bool]]
) -> dict[str, bool]:
    return {name: fn(value) for name, fn in rules.items()}


def max_length_rule(limit: int) -> Callable[[Any], bool]:
    """Return a rule that passes when len(value) <= limit."""
    return lambda v: len(v) <= limit
