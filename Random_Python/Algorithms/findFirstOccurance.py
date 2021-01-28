'''
    Find first index at which a given element occurs in a list
'''
def find(S, val):
    '''return index j such that S[j] == val, or -1 if no such element '''
    n = len(S)
    j = 0
    while j < n:
        if S[j] == val:
            return j  # match found at index j
        j += 1
    return -1  # no match found, return -1
