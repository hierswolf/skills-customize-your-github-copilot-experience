"""A simple calculator module to be tested by students."""


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference of two numbers."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return the quotient of two numbers.
    
    Raises ValueError if dividing by zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
