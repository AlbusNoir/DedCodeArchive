"""
    Accept input
    calculate # to bin
    output
"""


def numToBin():
    # first time int(input()) validation has actually been useful lol
    n = int(input('Enter a number: '))

    # define other vars for later
    number = n
    string = ''

    while number > 0:
        string = str(number % 2) + string  # modulo
        if number > 0:
            number = number // 2  # floor divide
    print(str(n) + ' is ' + string + ' in binary')

    repeat()


def repeat():  # I feel like I use this a lot...
    r = input('Convert another number? yN: ')
    if r.lower() == 'y':
        numToBin()
    else:  # lazy quit
        quit()


numToBin()
