def factors_of_n(n):
    """
    Return a list of the divisors of n with 1 and n included.
    """
    factors = []
    for i in range(1, n+1):
        if n % i == 0:
            factors.append(i)
    return factors


# a class of Prime would be more appropriate
# i would like to implement different algorithms of prime like sieve of eratosthenes,
# miller-rabin probability test, etc
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
    e.g. 84 has prime factorisation 2x2x3x7
    """
    factors = []
    divisor = 2
    while divisor <= n:
        if n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        else:
            divisor += 1
    return factors
# print(prime_factorisation(44))

def lcm(a, b):
    """
    Return the Lowest Common Multiple of a and b
    """
    if a == 0 and b == 0:
        return 0
    if a == b:
        return a

    pf_a = prime_factorisation(a)
    pf_b = prime_factorisation(b)

    # check for the shortest list to iterate over
    if len(pf_a) > len(pf_b):
        long_pf, short_pf = pf_a, pf_b
    else:
        long_pf, short_pf = pf_b, pf_a

    for p in short_pf:
        if p not in long_pf:
            long_pf.append(p)

    product = 1
    for n in long_pf:
        product = product * n
    
    return product

# print(lcm(144, 66))


    
def hcf(n1 , n2):
    """
    Return Highest Common Factor of n1 and n2.
    HCF is same as GCD.
    """
    if n1 > n2:
        a, b = n1, n2
    else:
        a, b = n2, n1

    if a == 1 and b == 1:
        return 1

    if b == 0:
        return a
    r = a % b
    a = a // b

    a = b
    b = r
    return hcf(a, b)


class Fraction():

    # def __init__():
        # a would be in the form a = "3/9"
        # b would be in the form a = "3/9"
        # self.a = a
        # self.b = b

    def split(self, fraction):
        split_fraction = fraction.split("/")
        numerator, denominator = int(split_fraction[0]), int(split_fraction[1])
        return numerator, denominator

    def simplify(self, a):
        if len(a) == 1:
            return a
        # split = a.split("/")
        # numerator, denominator = int(split[0]), int(split[1])
        
        numerator, denominator = split(a)
        cf = hcf(numerator, denominator)
        if int(denominator/cf) != 1:
            return f"{int(numerator/cf)}/{int(denominator/cf)}"
        return f"{int(numerator/cf)}"

    def add(self, a, b):
        # call simplify on the final result
        ...
    
    def multiply(self, a, b):
        # call simplify on the final result
        ...

    def divide(self, a, b):
        # call simplify on the final result
        ...

    