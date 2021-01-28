'''
    Ceasar Cipher using arrays
'''


class CeasarCipher:
    '''encrypt and decrypt cipher'''

    def __init__(self, shift):
        '''construct a cipher using given integer shift for rotation'''
        encoder = [None] * 52  # temp array for encryption
        decoder = [None] * 52  # temp array for decryption
        for k in range(52):
            encoder[k] = chr((k + shift) % 52 + ord('A'))
            decoder[k] = chr((k - shift) % 52 + ord('A'))
        self._forward = ''.join(encoder)  # store as str
        self._backward = ''.join(decoder)  # fixed msg

    def encrypt(self, message):
        '''return string representing encrypted message'''
        return self._transform(message, self._forward)

    def decrypt(self, secret):
        '''return decrypted msg given encrypted secret'''
        return self._transform(secret, self._backward)

    def _transform(self, original, code):
        '''util function to perform transformations'''
        # for WHATEVER reason this makes it accept lowercase, turns it to upper, then spits out the right upper. don't know how or why but whatev
        msg = list(original)
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord('A')  # index from 0 to 25
                msg[k] = code[j]  # replace this char
            elif msg[k].islower():
                i = ord(msg[k]) - ord('a')
                msg[k] = code[i]
        return ''.join(msg)


if __name__ == '__main__':
    '''cipher = CeasarCipher(3)  # shift 3
    message = 'THIS IS A TEST'
    coded = cipher.encrypt(message)
    print('Secret: ', coded)
    answer = cipher.decrypt(coded)
    print('Message: ', answer)'''

    cipher = int(input('Enter the amount you want to shift: '))
    cipher_int = CeasarCipher(cipher)
    message = input('Enter your message: ')
    coded = cipher_int.encrypt(message)
    print('Secret: ', coded)
    answer = cipher_int.decrypt(coded)
    print('Message: ', answer)
