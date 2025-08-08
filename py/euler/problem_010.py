from euler.problem_007 import sieve_of_eratosthenes


def solve() -> int:
    """
    Problem 010: Summation of primes
    """
    limit = 2_000_000
    result = sieve_of_eratosthenes(limit)
    return sum(result)
