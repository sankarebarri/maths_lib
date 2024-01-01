import math

from common_factor import *

def quadratic(a, b, c):
    determinant = b*b - 4*a*c
    if math.sqrt(determinant).is_integer():
        a_c = a * c
        factor_ac = factorisation(a_c)
        # return True
    return False

print(quadratic(3,-11,-4))