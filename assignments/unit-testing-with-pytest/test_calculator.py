"""Starter tests for the calculator module.

Run tests with:
    pytest test_calculator.py -v
    
Run with coverage report:
    pytest test_calculator.py --cov=calculator
"""

import pytest
from calculator import add, subtract, multiply, divide


# Task 1: Write basic unit tests.
# Add more test functions below to cover all operations and edge cases.

def test_add_positive_numbers():
    """Test adding two positive numbers."""
    assert add(2, 3) == 5


def test_add_negative_numbers():
    """Test adding two negative numbers."""
    assert add(-2, -3) == -5


def test_subtract_positive_numbers():
    """Test subtracting two positive numbers."""
    # TODO: Write this test.
    pass


def test_multiply_by_zero():
    """Test multiplying by zero."""
    # TODO: Write this test.
    pass


def test_divide_by_zero():
    """Test that dividing by zero raises an error."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(5, 0)


# Task 2: Use fixtures and parametrization.
# Uncomment and fill in the parametrize decorator and fixture below.

# @pytest.fixture
# def calculator_data():
#     """Fixture providing test data for calculator operations."""
#     return {
#         "add": [(2, 3, 5), (0, 0, 0), (-1, 1, 0)],
#         "subtract": [(5, 3, 2), (0, 0, 0), (-1, -1, 0)],
#         "multiply": [(2, 3, 6), (0, 5, 0), (-2, -3, 6)],
#     }


# @pytest.mark.parametrize("a,b,expected", [
#     (2, 3, 5),
#     (0, 0, 0),
#     (-1, 1, 0),
#     (100, 200, 300),
# ])
# def test_add_parametrized(a, b, expected):
#     """Test addition with multiple input combinations."""
#     assert add(a, b) == expected
