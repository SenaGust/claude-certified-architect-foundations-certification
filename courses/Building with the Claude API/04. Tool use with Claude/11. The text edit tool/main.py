def greeting():
    print("Hi there")


def calculate_pi_to_5th_digit():
    """
    Calculate pi to the 5th digit using the Machin formula:
    pi/4 = 4*arctan(1/5) - arctan(1/239)
    
    Returns:
        float: Pi calculated to at least 5 decimal places (3.14159...)
    """
    from decimal import Decimal, getcontext
    
    # Set precision high enough to get 5 decimal places accurately
    getcontext().prec = 50
    
    # Calculate arctan using Taylor series: arctan(x) = x - x^3/3 + x^5/5 - x^7/7 + ...
    def arctan(x, num_terms=100):
        x = Decimal(x)
        power = x
        result = power
        for n in range(1, num_terms):
            power *= -x * x
            result += power / (2 * n + 1)
        return result
    
    # Machin formula: pi/4 = 4*arctan(1/5) - arctan(1/239)
    pi = 4 * (4 * arctan(Decimal(1) / Decimal(5)) - arctan(Decimal(1) / Decimal(239)))
    
    return float(pi)