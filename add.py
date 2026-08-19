"""Basic addition module in Python."""

from typing import Union


def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Adds two numbers together and returns the sum.

    Args:
        a (Union[int, float]): The first number to add.
        b (Union[int, float]): The second number to add.

    Returns:
        Union[int, float]: The arithmetic sum of `a` and `b`.

    Examples:
        >>> add(2, 3)
        5
        >>> add(-1, 2.5)
        1.5
        >>> add(0, 0)
        0
    """
    return a + b
