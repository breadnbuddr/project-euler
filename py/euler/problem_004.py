def solve() -> int:
    """
    Problem 004: Largest palindrome product
    """
    largest_palindrome = 0

    for i in range(0, 1000):
        for j in range(0, 1000):
            product = i * j
            if is_palindrome(product) and product > largest_palindrome:
                largest_palindrome = product

    return largest_palindrome


def is_palindrome(n):
    s = str(n)
    return s == s[::-1]
