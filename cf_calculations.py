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
    cf = [] # cf = common factor
    divisors = divisors_of_n(n)
    for i in divisors:
        for j in divisors:
            if i * j == n:
                if (i,j) not in cf and (j, i) not in cf:
                    cf.append((i, j))
    return cf
# print(factorisation(18))

def diff_sum(x, y, b):
    """
    Different sums of x and y that equals b
    
    Parameters:
    -----------
        x: int
        y: int
        b: int

    Returns:
    --------
        tuple: if x + y == b
        None: if x + y != b
    """
    if x + y == b:
        return (x, y)
    elif -1*x + y == b:
        return (-1*x, y)
    elif x + -1*y == b:
        return (x, -1*y)
    elif -1*x + -1*y == b:
        return (-1*x, -1*y)
    else:
        return None

def hcf(n1, n2):
    # would like to extend the parameters to many
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
    return max(common_factor(n1, n2))

