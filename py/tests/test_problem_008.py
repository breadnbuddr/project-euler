from euler.problem_008 import solve


def test_problem_008():
    """
    Test for problem 008: Largest product in a series
    """
    assert (
        solve() == 23514624000
    ), "Expected the largest product in the series to be 23514624000, but got a different value."
