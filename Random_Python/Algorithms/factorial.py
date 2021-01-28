'''
    Factorial Recursion
    n! = 1 if n = 0 and n * (n-1)! if n >= 1
    That is 3 * 2 * 1 etc
'''
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
