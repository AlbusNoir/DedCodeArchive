'''
    Recursively calculate the power of a given number
'''


def power(x, n):
    '''computer value x**n for integer n'''
    if n == 0:
        return 1
    else:
        partial = power(x, n // 2)  # truncate
        result = partial * partial
        if n % 2 == 1:  # if n is odd, include extra factor of x
            result *= x
        return result
