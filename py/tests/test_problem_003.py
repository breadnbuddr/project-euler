from euler.problem_003 import solve


def test_problem_003():
    """
    Test for problem 003: Largest prime factor
    """
    assert solve() == 6857, "The largest prime factor of 600851475143 should be 6857"
