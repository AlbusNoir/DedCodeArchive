'''
    uses ArrayStack to match parenthesis
'''

def is_matched(expr):
    '''return True if all delimiters match'''
    lefty = '({['  # opening
    righty = ')}]'  #closing
    S = ArrayStack()

    for c in expr:
        if c in lefty:
            S.push(c)  # push left delimiter on stack
        elif c in righty:
            if S.is_empty():
                return False  # nothing to match with
            if righty.index(c) != lefty.index(S.pop()):
                return False  # mismatched
    return True  # all match
