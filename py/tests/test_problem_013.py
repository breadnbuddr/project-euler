from euler.problem_013 import solve


def test_problem_013():
    """
    Test for Problem for Problem 013: Large Sum
    """
    assert (
        solve() == 5537376230
    ), "Expected the sum of the first 100 50-digit numbers to be 5537376230, but got a different value."
