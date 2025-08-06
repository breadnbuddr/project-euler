def solve() -> int:
    """
    Problem 005: Smallest multiple
    """
    lcm = 1
    for i in range(1, 21):
        lcm = least_common_multiple(lcm, i)

    return lcm


def least_common_multiple(a: int, b: int):
    """
    Find the least common multiple (lcm) of two integers by using the relationship between lcm and gcd.
    """
    if a == 0 or b == 0:
        return 0
    return (a * b) // greatest_common_divisor(a, b)


def greatest_common_divisor(a: int, b: int) -> int:
    """
    Find the greatest common divisor (gcd) of two integers by using the modern Euclidean algorithm.
    """

    while b != 0:
        remainder = a % b
        a = b
        b = remainder

    return a
