def solve() -> int:
    """
    Problem 003: Largest prime factor
    """
    n = 600851475143
    primes = []
    prime = 2

    while n > 1:
        while n % prime == 0:
            primes.append(prime)
            n /= prime
        prime += 1

    return max(primes)
