import math

from cf_calculations import *

def quadratic(a, b, c):
    determinant = b*b - 4*a*c
    if math.sqrt(determinant).is_integer():
        a_c = abs(a) * abs(c) # multiplication of the 'a' term by the 'c' term
        # print(a_c)
        factor_ac = factorisation(a_c) # a list of pairs factors of a_c.
        # print(factor_ac)
        # look for the pairs in that list would equals the b term
        for factor in factor_ac:
            # print(diff_sum(factor[0], factor[1], b))
            if diff_sum(factor[0], factor[1], b) is not None:
                f_1, f_2 = diff_sum(factor[0], factor[1], b)
                break
        print(f"{a}x^2 + {f_1}x + {f_2}x + {c}")
        hcf_1 = hcf(a, f_1)
        if hcf_1 != 1:
            hcf_2 = hcf(f_2, c)
            print(f"{hcf_1}x({a/hcf_1}x + {f_1/hcf_1}) + {hcf_2}({f_2/hcf_2}x + {c/hcf_2})")
            print(f"({hcf_1}x + {hcf_2})({f_2/hcf_2}x + {c/hcf_2})")



    return

print(quadratic(6,11,3))