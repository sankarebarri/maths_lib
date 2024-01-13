import pytest

from arithmetic import *

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