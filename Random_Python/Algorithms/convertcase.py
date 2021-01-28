'''
    Got annoyed at the caesar cipher not giving me lowercase so I decided to make THIS
    It honestly DOESN'T do the same thing since this is strings and cipher is ints but whatever
'''


def convert_opposite(st):
    ln = len(st)

    for i in range(ln):
        if st[i] >= 'a' and st[i] <= 'z':
            # convert lower to upper
            st[i] = chr(ord(st[i]) - 32)

        elif st[i] >= 'A' and st[i] <= 'Z':
            # convert upper to lower
            st[i] = chr(ord(st[i]) + 32)


if __name__ == '__main__':
    print('Type words please:')
    st = input('> ')

    st = list(st)

    convert_opposite(st)

    st = ''.join(st)
    print(st)
