# 📘 Assignment: Unit Testing with pytest

## 🎯 Objective

Master professional testing practices by writing comprehensive unit tests for a calculator module. In this assignment, you will learn pytest fixtures, parametrized tests, edge cases, and how to organize test suites for maintainability.

## 📝 Tasks

### 🛠️	Write Basic Unit Tests

#### Description
Create test functions that verify the correct behavior of a calculator module. Each test should focus on a single function and cover both happy paths and edge cases.

#### Requirements
Completed program should:

- Write tests for addition, subtraction, multiplication, and division functions.
- Test normal cases (e.g., `2 + 2 = 4`).
- Test edge cases (e.g., negative numbers, zero, division by zero).
- Use `assert` statements to validate expected outcomes.
- Run tests with `pytest` and confirm all tests pass.


### 🛠️	Use Fixtures and Parametrization

#### Description
Refactor tests to reduce duplication by using pytest fixtures for setup/teardown and parametrized tests for running the same test logic over multiple inputs.

#### Requirements
Completed program should:

- Create a fixture that provides a calculator instance or test data.
- Use `@pytest.mark.parametrize` to run multiple test cases with different inputs in a single test function.
- Organize tests into a class or module for clarity.
- Generate a coverage report showing which lines of code are tested.
