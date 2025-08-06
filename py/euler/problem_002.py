def solve() -> int:
    """
    Problem 002: Even Fibonacci numbers
    """
    a = 1
    b = 2
    total = 0

    while a <= 4_000_000:
        if a % 2 == 0:
            total += a

        a, b = b, a + b

    return total
