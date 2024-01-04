import math

from cf_calculations import *
from lin_equation import linear_equation

def quadratic(a, b, c, show_step=False):
    determinant = b*b - 4*a*c
    if math.sqrt(determinant).is_integer():
        a_c = abs(a) * abs(c) # multiplication of the 'a' term by the 'c' term
        factor_ac = factorisation(a_c) # a list of pairs of factors of a_c.
        # look for the pairs in 'factor_ac list that would equals the b term
        for factor in factor_ac:
            if diff_sum(factor[0], factor[1], b) is not None:
                f_1, f_2 = diff_sum(factor[0], factor[1], b)
                break
        if show_step:
            print(f"{a}x^2 + {f_1}x + {f_2}x + {c}")
        hcf_1 = hcf(a, f_1) # common factor between 'a' in the equation and  f_1
        # no need of this condition
        if hcf_1 != 1:
            hcf_2 = hcf(f_2, c)
            if show_step:
                print(f"{hcf_1}x({a/hcf_1}x + {f_1/hcf_1}) + {hcf_2}({f_2/hcf_2}x + {c/hcf_2})")
                print(f"({hcf_1}x + {hcf_2})({f_2/hcf_2}x + {c/hcf_2})")
            equation_1 = f"{hcf_1}x + {hcf_2}"
            equation_2 = f"{f_2/hcf_2}x + {c/hcf_2}"
            # print(equation_1)
            # print(equation_2)
            x_1 = linear_equation(equation_1)
            x_2 = linear_equation(equation_2)
            print(x_1, x_2)



    return

print(quadratic(6,11,3))