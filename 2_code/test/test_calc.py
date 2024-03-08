import pytest
from code.calc import *

@pytest.fixture
def calculator():
    return Calculator()

@pytest.mark.calculator
def test_last_ans_after_init(calculator):
    assert calculator.ans == 0

@pytest.mark.calculator
@pytest.mark.parametrize("a,b,ans",
    [(2, 3, 5),
     (3, 2, 5)])
def test_plus(calculator, a, b, ans):
    calculator.plus(a, b)
    assert calculator.ans == ans

@pytest.mark.calculator
def test_delete(calculator):
    calculator.plus(5, 3)
    calculator.delete()
    assert calculator.ans == 0

@pytest.mark.calculator
@pytest.mark.parametrize("a,b,ans",
    [(3, 1, 0),
     (3, 2, 1)])
def test_modulo(calculator, a, b, ans):
    calculator.modulo(a, b)
    assert calculator.ans == ans

@pytest.mark.calculator
@pytest.mark.parametrize("a,b,c,ans",
    [(12, 16, 20, 1),
     (3, 2, 1, 0)])
def test_pythagoras(calculator, a, b, c, ans):
    calculator.pythagoras(a, b, c)
    assert calculator.ans == ans

# pip install pytest-cov
# python -m pytest --cov="." --cov-report=term
# python -m pytest --cov="." --cov-report=html:covhtml
# python -m pytest --cov="." --cov-report=xml:cov.xml
# python -m pytest --cov="." --cov-report=annotate
    
# pip install pytest-xdist
# python -m pytest -n 4
    
# pip install pytest-bdd
# python -m pytest test/test_calc.py::test_plus