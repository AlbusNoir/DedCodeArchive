'''
    Using stack, reverse a file
'''

def reverse_file(filename):
    '''overwrite a given file with its contents line-by-line reversed'''
    S = ArrayStack()  # references the arraystack prog in Classes
    original = open(filename)

    for line in original:
        S.push(line.rstrip('\n'))  # strip, newlines reinserted when writing
    original.close()

    # overwrite in LIFO order
    output = open(filename, 'w')  # reopn file and overwrites
    while not S.is_empty():
        output.write(S.pop() + '\n')  # reinsert newline chars
    output.close()
