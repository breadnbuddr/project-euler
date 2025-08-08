def solve() -> int:
    """
    Problem 9: Special Pythagorean triplet
    """
    for a in range(1, 1000):
        for b in range(a, 1000 - a):
            c = 1000 - a - b
            if a**2 + b**2 == c**2:
                return a * b * c
    return -1
