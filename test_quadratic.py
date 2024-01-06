from quadratic import quadratic_equation

def test_two_solution():
    # # 4x^2 + 12x + 9
    assert(quadratic_equation(4, 12, 9)) == (-1.5, -1.5)
    assert(quadratic_equation(1, 10, 24)) == (-6, -4)


def test_one_solution():
    ...

def test_no_solution():
    assert(quadratic_equation(4, 12, 2)) == "Can not be factored"
    assert(quadratic_equation(1, 6, 4)) == "Can not be factored"

def test_show_steps():
    ...