'''
    Linked dequeue
'''
class LinkedDequeue(_DoublyLinkedBase):
    '''double ended queue impl based on doubly linked list'''

    def first(self):
        '''return first'''
        if self.is_empty():
            raise Empty('Dequeue is empty')
        return self._header._next._element  # real item just after header

    def last(self):
        '''return last'''
        if self.is_empty():
            raise Empty('Dequeue is empty')
        return self._trailer._prev._element  # real item just before trailer

    def insert_first(self, e):
        '''add element to front'''
        self._insert_between(e, self._header, self._header._next)  # after header

    def insert_last(self, e):
        '''add element to back'''
        self._insert_between(e, self._trailer._prev, self._trailer)  # before trailer

    def delete_first(self):
        '''remove first'''
        if self.is_empty():
            raise Empty('Dequeue is empty')
        return self._delete_node(self._header._next)  # use inherited method

    def delete_last(self):
        '''remove last'''
        if self.is_empty():
            raise Empty('Dequeue is empty')
        return self._delete_node(self._trailer.prev)  # use inherited method
