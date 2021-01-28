"""
    Pass three parameters
    Define discriminant
    solve for roots if able
"""


def quadVars():
    a = int(input('Enter a: '))
    b = int(input('Enter b: '))
    c = int(input('Enter c: '))

    quadSolve(a, b, c)


def quadSolve(a, b, c):

    d = b ** 2 - 4 * a * c  # discriminant dec

    if d >= 0:
        e = (-b + d ** 0.5) / (2 * a)  # -b+sqrt(d)/2a
        f = (-b - d ** 0.5) / (2 * a)  # -b-sqrt(d)/2a

    if d < 0:
        print('No real solutions')  # handle neg discriminant, nonreal solution
    elif d == 0:
        print('X = ' + str(round(e)))  # only 1 real solution
    else:  # 2 real solutions
        print('X = ' + str(round(e)) + ' or ' + str(round(f)))

    repeat()


def repeat():
    r = input('Solve another equation? yN: ')
    if r.lower() == 'y':
        quadVars()
    else:  # lazy quit
        quit()


quadVars()
