'''
    Fibonacci using generators
'''


def fibonacci():
    a = 0
    b = 1
    while True:
        yield a  # show a during pass
        future = a + b  # start doin the switcheroo
        a = b  # next val
        b = future  # val after that

# because of msimultaneous assignment, we can alter this to the following
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b
