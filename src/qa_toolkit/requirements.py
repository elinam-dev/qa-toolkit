from typing import Any, Callable


def check_requirements(
    value: Any, rules: dict[str, Callable[[Any], bool]]
) -> dict[str, bool]:
    return {name: fn(value) for name, fn in rules.items()}
