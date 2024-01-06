import math

from cf_calculations import *
from lin_equation import linear_equation

def quadratic_equation(a, b, c, show_step=False):
    determinant = b*b - 4*a*c
    if math.sqrt(determinant).is_integer():
        a_c = abs(a) * abs(c)
        # print(a_c) # multiplication of the 'a' term by the 'c' term
        factor_ac = factorisation(a_c) # a list of pairs of factors of a_c.
        # print(factor_ac)
        # look for the pairs in 'factor_ac list that would equals the b term
        for factor in factor_ac:
            if diff_sum(factor[0], factor[1], b, a_c) is not None:
                b_1, b_2 = diff_sum(factor[0], factor[1], b, a_c)
                break
        if show_step:
            print(f"{a}x^2 + {b_1}x + {b_2}x + {c}")
        cf_1 = hcf(a, b_1) # common factor between 'a' in the equation and b_1
        # no need of this condition
        # if cf_1 != 1:
        cf_2 = hcf(b_2, c)
        if show_step:
            print(f"{cf_1}x({a/cf_1}x + {b_1/cf_1}) + {cf_2}({b_2/cf_2}x + {c/cf_2})")
            print(f"({cf_1}x + {cf_2})({b_2/cf_2}x + {c/cf_2})")
        equation_1 = f"{cf_1}x + {cf_2}"
        equation_2 = f"{b_2/cf_2}x + {c/cf_2}"
        # print(equation_1)
        # print(equation_2)
        x_1 = linear_equation(equation_1)
        x_2 = linear_equation(equation_2)
        return x_1, x_2
    else:
        return "Can not be factored"



# print(quadratic_equation(6,11,3))
# print(quadratic_equation(4,12,9))
# print(quadratic_equation(1,10,24))