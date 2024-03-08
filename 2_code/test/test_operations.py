import pytest
from code.operations import *

@pytest.mark.operation
@pytest.mark.parametrize("a,b,out",
    [(2, 3, 5),
     (3, 2, 5)])
def test_add(a, b, out):
    assert add(a, b) == out

# @pytest.mark.parametrize("a,b,out",
#     [(2, 3, -1),
#      (3, 2, 1)])
# def test_sub(a, b, out):
#     assert sub(a, b) == out

# @pytest.mark.parametrize("a,b,out",
#     [(2, 3, 6),
#      (3, 2, 6)])
# def test_mul(a, b, out):
#     assert mul(a, b) == out

# @pytest.mark.parametrize("a,b,out",
#     [(1, 2, 0.5),
#      (3, 2, 1.5)])
# def test_div(a, b ,out):
#     assert div(a, b) == out
    
@pytest.mark.operation
def test_div_zerodiv_exception():
    a, b = 5, 0
    with pytest.raises(ZeroDivisionError) as e:
        div(a, b)
    assert "division by zero" in str(e.value)