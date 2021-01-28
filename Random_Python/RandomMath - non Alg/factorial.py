''' factorials are the sum of a number and all numbers below that number
Accept user input, check for neg pos and 0, output
'''

# user input num
num = int(input('Enter a number: '))


factorial = 1


# check for neg pos or 0
if num < 0:
    print('Sorry, factorials can only be done on positive integers')
elif num == 0:
    print('The factorial of 0 is 1')
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print('The factorial of ',num,' is ',factorial)
