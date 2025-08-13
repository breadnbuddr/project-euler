from euler.problem_011 import solve


def test_problem_011():
    """
    Test for Problem for Problem 011: Largest product in a grid
    """
    assert (
        solve() == 70600674
    ), "Expected result for the largest product in a grid to be 70600674, but got a different value."
