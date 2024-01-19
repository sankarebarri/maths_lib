from treat_numbers import extract_numbers

def test_postive_negative():
    assert(extract_numbers("42+3")) == (42, 3)
    assert(extract_numbers("42 + 3")) == (42, 3)

    assert(extract_numbers("-42+3")) == (-42, 3)
    assert(extract_numbers("-42 + 3")) == (-42, 3)

    assert(extract_numbers("-42-3")) == (-42, -3)
    assert(extract_numbers("42-3")) == (42, -3)
    assert(extract_numbers("42 - 3")) == (42, -3)