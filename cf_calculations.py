"""
cf_calculations === common factors calculations
"""
def divisors_of_n(n):
    """Return a list of the divisors of n."""
    divisors_list = []
    for i in range(1, n+1):
        if n % i == 0:
            divisors_list.append(i)
    return divisors_list

def common_factor(n1, n2):
    # would like to extend the parameters to many
    """
    Return the list of the common factor between n1 and n2

    Parameters:
    -----------
        n1: int
        n2: int
    
    Returns:
    --------
        list
    """
    cf_list = [] # c_f = common factor
    n1_divisors = divisors_of_n(n1)
    n2_divisors = divisors_of_n(n2)

    # It would be better to use the intersection function
    for divisor in n1_divisors:
        if divisor in n2_divisors:
            cf_list.append(divisor)
    return cf_list

def factorisation(n):
    """
    Returns the list of factors of 'n' in pairs i.e of two numbers that multiply to n
    NB: It will will treat negative 'n' as positive n.
    """
    if n < 0:
        n = abs(n)
    cf = [] # cf = common factor
    divisors = divisors_of_n(n)
    for i in divisors:
        for j in divisors:
            if i * j == n:
                if (i,j) not in cf and (j, i) not in cf:
                    cf.append((i, j))
    return cf
# print(factorisation(18))

def diff_sum(x, y, b, c): # change name to diff_sum_prod
    """
    Different sums of x and y that equals b and whose products equal c.
    e.g. if x = 6, y = 4, b = 2, c = -24 it will return (-4, 6)
     
    Parameters:
    -----------
        x: int
        y: int
        b: int
        c: int

    Returns:
    --------
        tuple: if x + y == b
        None: if x + y != b
    """
    if (x + y == b) and (x * y == c):
        return (x, y)
    elif (-1*x + y == b) and (-1*x * y == c):
        return (-1*x, y)
    elif (x + -1*y == b) and (x * -1*y == c):
        return (x, -1*y)
    elif (-1*x + -1*y == b) and (-1*x * -1*y == c):
        return (-1*x, -1*y)
    else:
        return None
# print(diff_sum(6,4,10,24))

def hcf(n1, n2):
    # would like to extend the parameters to many
    # Implement it in euclidian algo
    """
    Return the highest common factor between n1 and n2.

    Parameters:
    -----------
        n1: int
        n2: int
    
    Returns:
    --------
        int
    """
    return max(common_factor(abs(n1), abs(n2)))
print(hcf(210, 45))
# a = factorisation(-24)
# print(a)
# for i in a:
#     print(diff_sum(i[0], i[1], 10, 24))

def factorise_equation(equation):
    """
    factorise simple linear equation like 2x + 10 = 2(x + 5)
    """
    ...