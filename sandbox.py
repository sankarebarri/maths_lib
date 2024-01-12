from cf_calculations import hcf
# eq = "2x + 10"

# if "+" in eq:
#     sign = "+"
# elif "-" in eq:
#     sign = "-"
# else:
#     sign = ""
# # split equations(collect like terms) functions would be more intresting here
# split = ['-2x ', ' 10']
# eq_split = eq.split("+")
# # print(eq_split)
# variable, constant = eq_split[0].strip(), int(eq_split[1].strip())
# variable_coeff = int(variable[:-1])
# # print(variable_coeff)
# if variable_coeff > 0 and sign == "+":
#     cf = hcf(variable_coeff, constant)
#     print(f"{cf}({variable_coeff/cf}x + {constant/cf})")
# if variable_coeff < 0 and sign == "+":

def factor(a, b):
    if a == 0:
        return b
    if a > 0 and b > 0:
        cf = hcf(a, b)
        return f"{cf}({a/cf}x + {b / cf})"
    else:
        return f"{cf}(x + {b // cf})"

print(factor(7, 10))
# print(factor(-2, 10))
# print(factor(2, -10))
# print(factor(-2, -10))
