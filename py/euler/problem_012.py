def solve() -> int:
    """
    Problem 12: Highly divisible triangular number
    """
    triangular_number = 0
    n = 1
    while True:
        triangular_number += n
        n += 1
        if number_of_divisors(triangular_number) > 500:
            return triangular_number


def number_of_divisors(n: int) -> int:
    """
    Calculate the number of divisors of a number n.
    """
    if n == 1:
        return 1

    count = 1
    prime = 2
    while prime * prime <= n:
        if n % prime == 0:
            exponent = 0
            while n % prime == 0:
                exponent += 1
                n //= prime
            count = count * (exponent + 1)
        prime += 1

    if n > 1:
        count *= 2

    return count
