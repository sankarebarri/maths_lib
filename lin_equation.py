def linear_equation(equation):
    if "+" in equation:
        sign = "+"
    else:
        sign = "-"
    split_equation = equation.split(sign)
    variable = split_equation[0].strip()
    constant = split_equation[1].strip()
    print(split_equation)
    print(variable, constant)
    if sign == "+":
        constant = -1 * float(constant)
    print(f"{variable} = {constant}")
    x = float(variable[0]) / float(constant)
    return x
print(linear_equation("3x+2"))