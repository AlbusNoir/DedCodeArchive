'''
    Use linear reursion to reverse a sequence
'''


def reverse(S, start, stop):
    '''reverse elements in implicit slice S[start:stop]'''
    if start < stop - 1:  # if at least 3 elements
        S[start], S[stop - 1] = S[stop - 1], S[start]  # swap first and last
        reverse(S, start + 1, stop - 1)  # recur rest
