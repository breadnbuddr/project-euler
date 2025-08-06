from euler.problem_002 import solve


def test_problem_002():
    """
    Test for problem 002: Even Fibonacci numbers
    """
    assert (
        solve() == 4613732
    ), "The sum of the even Fibonacci numbers not exceeding 4 million should be 4613732"
