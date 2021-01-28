"""
    Input
    Convert to Hex
    Output
"""


def numToHex():
    # oh look... more useful int(input())
    n = int(input('Enter a number: '))

    # define var for later
    # this is literally just a copy of numtoBin
    # it's about to change though...
    number = n
    string = ''

    # boom here's where it changes
    while number > 0:
        intlet = number % 16  # def this to handle num->hex

        if intlet >= 0 and intlet <= 9:
            string = str(intlet) + string
        elif intlet == 10:
            string = 'A' + string
        elif intlet == 11:
            string = 'B' + string
        elif intlet == 12:
            string = 'C' + string
        elif intlet == 13:
            string = 'D' + string
        elif intlet == 14:
            string = 'E' + string
        else:
            string = 'F' + string

    if number > 0:
        number = number // 16  # floor divide

    print(str(n) + ' is ' + string + ' in Hex')

    repeat()


def repeat():  # this again...
    r = input('Convert another number? yN: ')
    if r.lower() == 'y':
        numToHex()
    else:  # lazy quit
        quit()


numToHex()
