'''
    this is the reverse of halfpyramid.py
'''


def reverse_pyramid():
    rows = int(input('How many rows: '))

    # num spaces
    r = 2 * rows - 2

    for i in range(0, rows):
        for j in range(0, r):
            print(end=' ')

        r = r - 2  # decrement

        for j in range(0, i + 1):
            print('* ', end='')

        print('\r')


reverse_pyramid()
