from euler.problem_004 import solve


def test_problem_004():
    """
    Test for problem 004: Largest palindrome product.
    """
    assert (
        solve() == 906609
    ), "The largest palindrome made from the product of two 3-digit numbers should be 906609"
