'''
    uses arraystack class to match html tags
'''

def is_matched_html(raw):
    '''return True if all html tags match'''
    S = ArrayStack()
    j = raw.find('<')  # find first opening char
    while j != -1:
        k = raw.find('>', j + 1)  # find next char
        if k == -1:
            return False  # invalid tag
        tag = raw[j + 1:k]  # strip away <>
        if not tag.startswith('/'):  # this is opening tag
            S.push(tag)
        else:  # this is a closing tag
            if S.is_empty():
                return False  # nothing to match
            if tag[1:] != S.pop():
                return False  # mismatched tag
        j = raw.find('<', k + 1)  # find next < char
    return S.is_empty()  # were all tags matched?
