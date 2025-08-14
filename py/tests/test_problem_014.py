from euler.problem_014 import solve


def test_problem_014():
    """
    Test for Problem for Problem 014: Longest Collatz sequence
    """
    assert (
        solve() == 837799
    ), "Expected the longest Collatz sequence starting number to be 837799, but got a different result."
