"""
    Euclid's Algorithm is super old. Like 300BCE old
    It's used to find GCD (Greatest Common Divider)
"""


def getFactors():
    a = int(input('Enter value for a: '))
    b = int(input('Enter value for b: '))

    euclid(a, b)


def euclid(a, b):
    while b != 0:
        a, b = b, a % b
    print(a)

    repeat()


def repeat():
    r = input('Find another GCD? yN: ')
    if r.lower() == 'y':
        getFactors()
    else:  # lazy quit
        quit()


getFactors()
