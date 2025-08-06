# import pytest
from euler.problem_001 import solve


# @pytest.mark.xfail(reason="Not solved yet")
def test_problem_001():
    """
    Test for problem 001: Multiples of 3 and 5
    """
    assert (
        solve() == 233168
    ), "The sum of all multiples of 3 or 5 below 1000 should be 233168"
