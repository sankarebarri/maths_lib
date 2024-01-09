from quadratic import quadratic_equation

def test_abc_provided():
    assert(quadratic_equation(1, 10, 24)) == (-6, -4) # x^2 + 10x + 24
    assert(quadratic_equation(-1, 12, -35)) == (5, 7) # -x^2 + 12x - 35
    # assert(quadratic_equation(-1, 12, -35)) == (-3, 1) # -x^2 - 2x + 3

    assert(quadratic_equation(4, 12, 9)) == (-1.5, -1.5) # 4x^2 + 12x + 9
    assert(quadratic_equation(-6, 3, 3)) == (-1.5, 1) # -6x^2 + 3x + 3


def test_b_not_provided():
    assert(quadratic_equation(1, 0, -9)) == (-3, 3) # x^2 - 9
    assert(quadratic_equation(-1, 0, 9)) == (-3, 3) # -x^2 + 9

    assert(quadratic_equation(9, 0, -16)) == (-1.33, 1.33) # 9x^2 - 16
    assert(quadratic_equation(-9, 0, 16)) == (-1.33, 1.33) # -9x^2 + 16

def test_c_not_provided():
    assert(quadratic_equation(1, 3, 0)) == (-3, 0) # x^2 + 3x
    assert(quadratic_equation(-1, 3, 0)) == (0, 3) # -x^2 + 3x

    assert(quadratic_equation(6, 3, 0)) == (-1.5, 0) # 6x^2 + 3x
    assert(quadratic_equation(-6, 3, 0)) == (0, 1.5) # -6x^2 + 3x

def test_show_steps():
    ...

def test_no_solution():
    assert(quadratic_equation(4, 12, 2)) == "Can not be factored"
    assert(quadratic_equation(1, 6, 4)) == "Can not be factored"