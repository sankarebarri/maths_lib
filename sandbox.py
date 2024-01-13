# import re
# # from cf_calculations import hcf
# # # eq = "2x + 10"

# # if "+" in eq:
# #     sign = "+"
# # elif "-" in eq:
# #     sign = "-"
# # # else:
# # #     sign = ""
# # # # split equations(collect like terms) functions would be more intresting here
# # # split = ['-2x ', ' 10']
# # # eq_split = eq.split("+")
# # # # print(eq_split)
# # # variable, constant = eq_split[0].strip(), int(eq_split[1].strip())
# # # variable_coeff = int(variable[:-1])
# # # # print(variable_coeff)
# # # if variable_coeff > 0 and sign == "+":
# # #     cf = hcf(variable_coeff, constant)
# # #     print(f"{cf}({variable_coeff/cf}x + {constant/cf})")
# # # if variable_coeff < 0 and sign == "+":

# from cf_calculations import hcf
# def factorise_linear_equation(equation):
#     equation = equation.replace(" ", "")
#     a, b = re.findall(r'[+-]?\d*\.?\d+', equation)
#     a, b = int(a), int(b)
        
#     if a == 0:
#         return b
#     if b == 0:
#         return f"{a}x"
#     cf = hcf(abs(a), abs(b))
#     # print(cf)
#     if a > 0 and b > 0:
#         return f"{cf}({a // cf}x + {b // cf})"
#     elif a > 0 and b < 0:
#         return f"{cf}({a // cf}x - {abs(b // cf)})"
#     elif a < 0 and b > 0:
#         return f"-{cf}({abs(a // cf)}x - {b // cf})"
#     else:
#         return f"-{cf}({abs(a // cf)}x + {abs(b // cf)})"

# print(factorise_linear_equation("2x + 10"))
# print(factorise_linear_equation("2x - 10"))
# print(factorise_linear_equation("-2x + 10"))
# print(factorise_linear_equation("-2x - 10"))
# # print(hcf(5,10))

# # def gcd(n1 , n2):
# #     a, b = max(n1, n2), min(n1, n2)
# #     if a == 1 and b == 1:
# #         return 1

# #     if b == 0:
# #         return a
# #     r = a % b
# #     a = a // b

# #     a = b
# #     b = r
# #     return gcd(a, b)
# # print(gcd(100, 20))

a = [2,3,5,7]
a_i = iter(a)

f = a[0]
num = 84
while num%f == 0:
    print(num/f)
    num = num / 2
    if 84%f != 0:
        f = next(a_i)