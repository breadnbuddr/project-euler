from euler.problem_010 import solve


def test_problem_010():
    """
    Test for Problem 010: Summation of primes
    """
    assert (
        solve() == 142913828922
    ), "Expected the sum of all primes below 2 million to be 142913828922, but got a different value."
