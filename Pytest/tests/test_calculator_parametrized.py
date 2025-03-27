import pytest
from src import calculator

def test_add():
    assert calculator.add(1,2) == 3
    assert calculator.add(0,5) == 5
    assert calculator.add(-2,9) == 7
    assert calculator.add(5, -8) == -3

def test_add_2():
    assert calculator.add_wrong(1,2) == 3
    assert calculator.add_wrong(0,5) == 5
    assert calculator.add_wrong(-2,9) == 7
    assert calculator.add_wrong(0,0) == 0

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (0, 5, 5),
        (-2, 9, 7),
        (5, -8, -3),
    ],
)
def test_add_parametrized(a, b, expected):
    assert calculator.add(a, b) == expected

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (0, 5, 5),
        (-2, 9, 7),
        (5, -8, -3),
    ],
)
def test_add_wrong_parametrized(a, b, expected):
    assert calculator.add_wrong(a, b) == expected

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 1, 1),
        (5, 0, 5),
        (8, 3, 5),
        (7, 4, 3),
    ],
)
def test_subtract_parametrized(a, b, expected):
    assert calculator.subtract(a, b) == expected

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 2),
        (0, 5, 0),
        (2, 9, 18),
        (5, 8, 40),
    ],
)
def test_multiply_parametrized(a, b, expected):
    assert calculator.multiply(a, b) == expected

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 2),
        (0, 5, 0),
        (2, 9, 18),
        (5, 8, 40),
    ],
)
def test_multiply_wrong_parametrized(a, b, expected):
    assert calculator.multiply_wrong(a, b) == expected

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (4, 2, 2),
        (10, 5, 2),
        (18, 2, 9),
        (40, 8, 5),
    ],
)
def test_divide_parametrized(a, b, expected):
    assert calculator.divide(a, b) == expected

@pytest.mark.parametrize(
    "a, b, expected_expection, expected_msg",
    [
        (0, 5, ValueError, "Cannot take log of non-positive number!"),
        (-2, 5, ValueError, "Cannot take log of non-positive number!"),
        (9, -2, ZeroDivisionError, "Cannot take log with non-positive base!"),
        (5, 1, NameError, "Cannot take log with base 1!"),
    ],
)
def test_log(a, b, expected_expection, expected_msg):
    with pytest.raises(expected_expection) as exc:
        calculator.log(a, b)
    assert str(exc.value) == expected_msg



