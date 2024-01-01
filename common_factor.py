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
    cf_list = []
    n1_divisors = divisors_of_n(n1)
    n2_divisors = divisors_of_n(n2)

    # It would be better to use the intersection function
    for divisor in n1_divisors:
        if divisor in n2_divisors:
            cf_list.append(divisor)
    return cf_list

def factorisation(n):
    cf = []
    divisors = divisors_of_n(n)
    for i in divisors:
        for j in divisors:
            if i * j == n:
                if (i,j) not in cf and (j, i) not in cf:
                    cf.append((i, j))
    return cf
print(factorisation(12))

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