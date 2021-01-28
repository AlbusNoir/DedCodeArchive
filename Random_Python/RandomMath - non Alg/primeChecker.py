"""
    Prompt for input
    Pass number into check
    Output
"""


def prime_check():
    num = int(input('Enter number to check for Primality: '))

    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(num, 'is not Prime')
                print(i, 'times', num // i, 'is', num)
                repeat()
        else:
            print(num, 'is Prime')
            repeat()

    else:  # num is 1 or is less than 1
        if num == 1:
            print('1 itself is not Prime')
        else:
            print(num, 'is not Prime')
        repeat()


def repeat():
    r = input('Check Primality of another number? yN: ')
    if r.lower() == 'y':
        prime_check()
    else:
        quit()  # lazy quit


prime_check()
