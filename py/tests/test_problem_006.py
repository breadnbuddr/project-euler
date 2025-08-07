from euler.problem_006 import solve


def test_problem_006():
    """
    Test for Project Euler Problem 6: Sum square difference
    """
    assert (
        solve() == 25164150
    ), "The solution to Problem 6 is incorrect. Expected 25164150."
