def solve() -> int:
    """
    Problem 014: Longest Collatz sequence
    """
    max_length = 0
    number_with_max_length = 0

    for i in range(1, 1000000):
        length = collatz(i)
        if length > max_length:
            max_length = length
            number_with_max_length = i

    return number_with_max_length


def collatz(n: int) -> int:
    """
    Calculate the number of steps to reach 1 in the Collatz sequence starting from n.
    """
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps
