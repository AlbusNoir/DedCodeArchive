'''
    Favorites list with move to front heuristic
'''
class FavoritesListMTF:
    '''heuristic that moves favorites to front'''


    # override _move_up o provide move to front
    def _move_up(self, p):
        '''move accessed p to front of list'''
        if p != self._data.first():
            self._data.add_first(self._data.delete(p))  # delete/reinsert

    # override top bc list no longer sorted
    def top(self, k):
        '''generate seq of top k ele in terms of count'''
        if not 1 <= k <= len(self):
            raise ValueError('Illegal value for k')

        # make copy of orig list
        temp = PositionalList()
        for item in self._data:  # iteration
            temp.add_list(item)

        # find, report, remove
        for j in range(k):
            # find and report
            highPos = temp.first()
            walk = temp.after(highPos)
            while walk is not None:
                if walk.element()._count > highPos.element()._count:
                    highPos = walk
                walk = temp.after(walk)
            # found ele with highest count
            yield highPos.element()._value  # rep to user
            temp.delete(highPos)  # remove from temp
