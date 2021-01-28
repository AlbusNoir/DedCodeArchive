'''
    3 way disjointness compare elements in three lists and returns True if no elements are shared and returns False if there are shared elements
'''


def disjoint1(A, B, C):
    '''return True if no element in common'''
    for a in A:
        for b in B:
            for c in C:
                if a == b == c:
                    return False  # found common
    return True  # found no common


''' better way to write this'''
def disjoint2(A, B, C):
    '''return True is no element in common'''
    for a in A:
        for b in B:
            if a == b:  # only check C if a == b
                for c in C:
                    if a == c:  # at this point, a == b == c
                        return False  # found common
    return True  # no common
