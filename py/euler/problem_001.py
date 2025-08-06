def solve() -> int:
    """
    Problem 001: Multiples of 3 and 5
    """
    return sum(n for n in range(0, 1000) if n % 3 == 0 or n % 5 == 0)
