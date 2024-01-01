from common_factor import hcf

def test_direct_factor():
    assert hcf(15, 3) == 3
    assert hcf(27, 9) == 9
    assert hcf(25, 1) == 1
    assert hcf(12, 4) == 4

def test_indirect_factor():
    assert hcf(15, 9) == 3
    assert hcf(27, 18) == 9
    assert hcf(12, 16) == 4

def test_no_factor():
    assert hcf(15, 7) == 1
    assert hcf(27, 25) == 1
    assert hcf(7, 16) == 1