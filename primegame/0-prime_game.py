#!/usr/bin/python3
"""Prime Game: determine who wins the most rounds."""


def isWinner(x, nums):
    """Return the name of the player who won the most rounds, or None.

    Each move removes exactly one prime (with its multiples), so a round
    lasts as many moves as there are primes <= n. Maria wins a round when
    that count is odd, Ben when it is even.
    """
    if not nums or x < 1:
        return None

    rounds = nums[:x]
    max_n = max(rounds)
    if max_n < 1:
        return "Ben"

    # Sieve of Eratosthenes up to max_n
    sieve = [True] * (max_n + 1)
    sieve[0] = False
    if max_n >= 1:
        sieve[1] = False
    i = 2
    while i * i <= max_n:
        if sieve[i]:
            for j in range(i * i, max_n + 1, i):
                sieve[j] = False
        i += 1

    # prime_count[k] = number of primes <= k
    prime_count = [0] * (max_n + 1)
    count = 0
    for k in range(max_n + 1):
        if sieve[k]:
            count += 1
        prime_count[k] = count

    maria = 0
    ben = 0
    for n in rounds:
        if n > 0 and prime_count[n] % 2 == 1:
            maria += 1
        else:
            ben += 1

    if maria > ben:
        return "Maria"
    if ben > maria:
        return "Ben"
    return None
