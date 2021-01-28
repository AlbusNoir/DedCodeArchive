# find LCM using GCD
# GCD function
def gcd(x, y):
    # uses euclidian alg to find GCD
    while(y):
        x, y = y, x % y

    return x

# LCM function
def lcm(x, y):
    # take two ints and return LCM
    lcm = (x*y)//gcd(x,y)
    return lcm


# take user input
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))


print('The LCM of', num1, 'and', num2, 'is', lcm(num1, num2))
