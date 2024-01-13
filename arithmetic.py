def is_prime(n):
    """
    Return True if n is prime. False if it is not
    """
    if n < 0:
        raise ValueError(f"You type in a negative number: {n}")

    if type(n) is not int:
        raise TypeError("You must type in a number")

    if n == 1 or n == 0:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def primes_leq_n(n):
    """
    Return list of prime numbers that are less than or equals to n
    """
    primes = []
    if n == 2:
        return [2]
    for i in range(2, n+1):
        if is_prime(i):
            primes.append(i)
    return primes

def prime_factorisation(n):
    """
    Return the list of prime factorisation of n
    """
    factors = []
    divisor = 2
    while divisor <= n:
        if n % divisor == 0:
            factors.append(divisor)
            divisor = n // divisor
        else:
            divisor += 1
    return factors


def lcm(a, b):
    ...

def hcf(a, b):
    ...
    