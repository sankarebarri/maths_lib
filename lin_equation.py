def factor_equation(equation):
    ...

def collect_like_terms(equation):
    ...

def linear_equation(equation, n=2):
    if "+" in equation:
        sign = "+"
    else:
        sign = "-"
    split_equation = equation.split(sign)
    variable = split_equation[0].strip()
    constant = split_equation[1].strip()
    if sign == "+":
        constant = -1 * float(constant)
    x = float(constant) / float(variable[0])
    if n:
        return round(x, n)
    return round(x, 2)

# print(linear_equation("3x+26"))
# print(linear_equation("3x+26", n=4))