'''
    Found a c++ code snippet on pinterest
    wanted to reproduce in python
    sooo made this
'''


def half_pyramid():
    rows = int(input('How many rows: '))

    if rows == 0:
        raise ValueError('Rows cannot be 0')
    else:
        for i in range(0, rows):
            for j in range(0, i + 1):
                print('* ', end='')
            print('\r')  # reset for nxt ln


half_pyramid()
