import pytest

from arithmetic import *

def test_factors_of_n():
    assert(factors_of_n(0)) == []
    assert(factors_of_n(1)) == [1]
    assert(factors_of_n(2)) == [1,2]
    assert(factors_of_n(18)) == [1,2,3,6,9,18]

def test_is_prime():
    assert(is_prime(1)) == False
    assert(is_prime(2)) == True
    assert(is_prime(0)) == False
    assert(is_prime(97)) == True

    with pytest.raises(ValueError):
        assert(is_prime(-2))

    with pytest.raises(TypeError):
        assert(is_prime("string"))


def test_prime_leq_n():
    assert(primes_leq_n(0)) == []
    assert(primes_leq_n(1)) == []

    assert(primes_leq_n(2)) == [2]

    assert(primes_leq_n(7)) == [2,3,5,7]
    assert(primes_leq_n(8)) == [2,3,5,7]

    assert(primes_leq_n(20)) == [2,3,5,7,11,13,17,19]

    assert(primes_leq_n(-2)) == []
    assert(primes_leq_n(-9)) == []


def test_prime_factorisation():
    assert(prime_factorisation(0)) == []
    assert(prime_factorisation(1)) == []

    assert(prime_factorisation(2)) == [2]
    assert(prime_factorisation(84)) == [2,2,3,7]
    assert(prime_factorisation(126)) == [2,3,3,7]


def test_lcm():
    assert(lcm(0, 0)) == 0
    assert(lcm(1, 1)) == 1
    assert(lcm(4, 8)) == 8
    assert(lcm(144, 66)) == 1584
    assert(lcm(512, 84)) == 10752
    assert(lcm(1000, 1000)) == 1000

def test_hcf():
    assert(hcf(0, 0)) == 0
    assert(hcf(1, 1)) == 1
    assert(hcf(4, 8)) == 4
    assert(hcf(144, 66)) == 6
    assert(hcf(512, 84)) == 4
    assert(hcf(1000, 1000)) == 1000

def test_fraction():
    f = Fraction(3, 9)

    assert(f.reduce_fraction()) == "1/3"
    assert(f.add()) == "3/7"
    assert(f.multiply()) == "8/9"
    assert(f.divide()) == "7/5"