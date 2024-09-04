from treat_numbers import extract_numbers

def test_single_number():
    assert(extract_numbers("43")) == 43
    assert(extract_numbers("3")) == 3
    assert(extract_numbers("0")) == 0
    assert(extract_numbers("-3")) == -3

def test_postive_negative():
    assert(extract_numbers("42+3")) == (42, 3)
    assert(extract_numbers("42 + 3")) == (42, 3)

    assert(extract_numbers("-42+3")) == (-42, 3)
    assert(extract_numbers("-42 + 3")) == (-42, 3)

    assert(extract_numbers("-42-3")) == (-42, -3)
    assert(extract_numbers("42-3")) == (42, -3)
    assert(extract_numbers("42 - 3")) == (42, -3)

def test_multiple_division():
    assert(extract_numbers("42/3")) == (42, 3)
    assert(extract_numbers("42 / 3")) == (42, 3)

    assert(extract_numbers("42*3")) == (42, 3)
    assert(extract_numbers("42 * 3")) == (42, 3)
