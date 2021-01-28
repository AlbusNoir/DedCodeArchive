'''Uniqueness checks
    checks for unique elements in a sequence
    returns True if all unique
    returns False otherwise
'''
def unique1(S):
    '''returns True if no duplicate elements'''
    for j in range(len(S)):
        for k in range(j+1, len(S)):
            if S[j] == S[k]:
                return False  # found a match
    return True  # all elements unique


'''different method'''
def unique2(S):
    '''returns True if no duplicates'''
    temp = sorted(S)  # create sorted copy of S
    for j in range(1, len(temp)):
        if S[j - 1] == S[j]:
            return False  # found duplicate
    return True  # no duplicates
