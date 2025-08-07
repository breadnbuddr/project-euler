from euler.problem_007 import solve


def test_problem_007():
    """
    Test for Problem 007: 10001st prime
    """
    assert (
        solve() == 104743
    ), "Expected the 10001st prime to be 104743, but got a different value."
