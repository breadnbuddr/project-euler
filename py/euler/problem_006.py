def solve() -> int:
    """
    Project Euler Problem 6: Sum square difference
    """
    sum_of_squares = 0
    for i in range(1, 101):
        sum_of_squares += i**2

    sum = 0
    square_of_sum = 0
    for i in range(1, 101):
        sum += i
        square_of_sum = sum**2

    sum_square_difference = square_of_sum - sum_of_squares

    return sum_square_difference
