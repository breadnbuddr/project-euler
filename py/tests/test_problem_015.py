from euler.problem_015 import solve


def test_problem_015():
    """
    Test for Problem 015: Lattice paths
    """
    assert (
        solve() == 137846528820
    ), "Expected the number of lattice paths through a 20x20 grid to be 137846528820, but got a different value."
