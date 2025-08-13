from euler.problem_012 import solve


def test_problem_012():
    """
    Test for Problem for Problem 012: Highly divisible triangular number
    """
    assert (
        solve() == 76576500
    ), "Expected the first triangular number with over 500 divisors to be 76576500, but got a different value."
