from cf_calculations import *

a = factorisation(12)
# b = 18
# c, d = 2, 9

def diff_sum(x, y, b):
    if x + y == b:
        return (x, y)
    elif -1*x + y == b:
        return (-1*x, y)
    elif x + -1*y == b:
        return (x, -1*y)
    elif -1*x + -1*y == b:
        return (-1*x, -1*y)

# print(diff_sum(1, 12, -11))
# for factor in a:
#     print(factor[0], factor[1])
#     print(diff_sum(factor[0], factor[1], 11))
# print(common_factor(6, 9))
# print(hcf(7, 9))