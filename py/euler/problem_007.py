def solve() -> int:
    """
    Problem 007: 10001st prime
    """
    primes = sieve_of_eratosthenes(200_000)
    return primes[10_000]


def sieve_of_eratosthenes(n: int) -> list:
    """
    Returns a list of prime numbers up to n using the Sieve of Eratosthenes.
    """
    prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    primes = []
    for p in range(2, n + 1):
        if prime[p]:
            primes.append(p)

    return primes
