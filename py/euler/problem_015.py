def solve() -> int:
    """
    Problem 15: Lattice paths
    """

    # The number of routes through a 20x20 grid is given by the binomial coefficient C(40, 20).
    return binomial_coefficient(40, 20)


def binomial_coefficient(n: int, k: int) -> int:
    """
    Calculate the binomial coefficient C(n, k) = n! / (k! * (n - k)!)
    """
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1

    k = min(k, n - k)
    result = 1
    for i in range(k):
        result = result * (n - i) // (i + 1)
    return result
