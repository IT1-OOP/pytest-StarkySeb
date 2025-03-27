from src import calculator
import pytest



def test_devide():
    with pytest.raises(ValueError) as exc:
        calculator.divide(5, 0)
    assert str(exc.value) == "Cannot divide by zero!"

def test_divide2():
    with pytest.raises(ValueError):
        assert calculator.divide(8,0) == 4