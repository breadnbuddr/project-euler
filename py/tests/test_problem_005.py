from euler.problem_005 import solve


def test_problem_005():
    """
    Test for problem 005: Smallest multiple
    """
    assert (
        solve() == 232792560
    ), "Expected the smallest multiple of numbers 1 to 20 to be 232792560"
