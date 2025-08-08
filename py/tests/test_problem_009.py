from euler.problem_009 import solve


def test_problem_009():
    """
    Test for problem 009: Special Pythagorean triplet.
    """
    assert (
        solve() == 31875000
    ), "Expected the product of the special Pythagorean triplet to be 31875000, but got a different value."
