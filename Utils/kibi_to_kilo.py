# Will was doing some kind of thing in linux
# he needs kibibytes converted to kilobytes
# i had to learn math to do this so like yeah
# anyway, here's math


'''Formulas:
   kib to kb: 1000 * (KiB / 1024)
   kb to kib: 1024 * (kb / 1000)
'''

prompt = int(input('''Please select from the following:
          1: I know the kibibytes
          2: I know the kilobytes
          > '''))

# equations
if prompt == 1:
    print('Please enter the kibibytes, with no comma\n')
    kib = int(input('> '))

    kb = (1024 * (kib / 1000))
    print(f'{kib} kib is equal to {kb} kb')

elif prompt == 2:
    print('Please enter the kilobytes, with no commas\n')
    kb = int(input('> '))

    kib = (1000 * (kb / 1024))
    print(f'{kb} kb is equal to {kib} kib')

else:
    print('Input not handled')
