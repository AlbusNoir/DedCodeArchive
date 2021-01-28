'''
    sort a positional list
'''

def insertion_sort(L):
    '''sort postional list of comparable elements into nondecreasing order'''
    if len(L) > 1:  # no need to sort otherwise
        marker = L.first()
        while marker != L.last():
            pivot = L.after(marker)  # next item
            value = pivot.element()
            if value > marker.element():  # pivot sorted
                marker = pivot  # pivot becomes marker
            else:  # relocate pivot
                walk = marker  # find leftmost item of greater value
                while walk != L.last() and L.before(walk).element() > value:
                    walk = L.before(walk)
                L.delete(pivot)
                L.add_before(walk, value)  # reinsert value before walk
