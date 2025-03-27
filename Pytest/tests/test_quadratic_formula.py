from src import calculator
import pytest


def test_quadratic_formula():
     assert calculator.solve_quadratic_formula(1, -3, 2) == (2.0, 1.0)
     assert calculator.solve_quadratic_formula(1, 4, -12) == (2, -6) 

@pytest.mark.parametrize(
    "a, b, c, expected, ",
    [
        (1, -3, 2, (2.0, 1.0)),  
        (1, -4, 4, (2.0, 2.0)),  
        (1, 0, -4, (2.0, -2.0)),  
    ]
)
def test_solve_quadratic_formula(a, b, c, expected):
    assert calculator.solve_quadratic_formula(a, b, c) == expected

@pytest.mark.parametrize(
    "a, b, c, expected_exception, expected_msg",
    [
        
        ("a", -3, 2, TypeError, "All coefficients must be of type float or int!"),  
        (0, -4, 4, SyntaxError, "Cannot solve quadratic formula with a = 0!"), 
        (1, 5, 2, NameError, "I don't like when b = 5!"),  
        (1, 2, 5, ValueError, "Cannot solve quadratic formula with negative discriminant!"), 
    ],
)
def test_exception(a, b, c, expected_exception, expected_msg):
    with pytest.raises(expected_exception) as exc:
        calculator.solve_quadratic_formula(a, b, c)
    assert str(exc.value) == expected_msg