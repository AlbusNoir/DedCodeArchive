'''
    List of elements from most frequent to least
'''
class FavoritesList:
    '''list elements from most to least freq'''

    #------------nested _Item class------------
    class _Item:
        __slots__ = '_value', '_count'  # for mem
        def __init__(self, e):
            self._value = e  # user's element
            self._count = 0  # initial count = 0

    #-----------nonpublic utilities-------------
    def _find_position(self, e):
        '''search for e and return postition'''
        walk = self._data.first()
        while walk is not None and walk.element()._value != e:
            walk = self._data.after(walk)
        return walk

    def _move_up(self, p):
        '''move item at position p in list based on access count'''
        if p != self._data.first():  # consider moving
            cnt = p.element()._count
            walk = self._data.before(p)
            if cnt > walk.element()._count:  # shift forward
                while(walk != self._data.first() and cnt > self._data.before(walk).element()._count):
                    walk = self._data.before(walk)
                self._data.add_before(walk, self._data.delete(p))  # delete/reinsert

    #------------public methods----------------
    def __init__(self):
        '''create empty fave list'''
        self._data = PositionList()  # list of _Item instances

    def __len__(self):
        '''return num entries'''
        return len(self._data)

    def is_empty(self):
        '''return True is empty'''
        return len(self._data) == 0

    def access(self, e):
        '''access element e thereby increasing count'''
        p = self._find_position(e)  # try to locate
        if p is None:
            p = self._data.add_last(self._Item(e))  # if new, place at end
        p.element()._count += 1  # increment count
        self._move_up(p)  # consider move forward

    def remove(self, e):
        '''remove e from list of faves'''
        p = self._find_position(e)  # locate
        if p is not None:
            self._data.delete(p)  # delete if found

    def top(self, k):
        '''gen seq of top k elements in term of access count'''
        if not 1 <= k <= len(self):
            raise ValueError('Illegal value for k')
        walk = self._data.first()
        for j in range(k):
            item = walk.element()  # ele of list is _Item
            yield item._value  # report user's element
            walk = self._data.after(walk)
