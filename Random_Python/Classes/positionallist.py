'''
    Complex class for positional list
    allows positional access to elements
'''
class PositionalList:
    #------------nested position class-----------
    class Position:
        '''abstract class representing location of a single element'''

        def __init__(self, container, node):
            '''constructor not to be invoked by user'''
            self._container = container
            self._node = node

        def element(self):
            '''return element store at this position'''
            return self._node._element

        def __eq__(self, other):
            '''return True if other is in same position'''
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            '''return true if other is not same position'''
            return not (self == other)  # opposite of __eq__

    #------------utility method---------------
    def _validate(self, p):
        '''return position's node or raise appropriate error'''
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._next is None:
            raise ValueError('p is no longer valid')
        return p._node

    #-------------utility method----------------
    def _make_position(self, node):
        '''return position instance for givennode(or none if sentinel)'''
        if node is self._header or node is self._trailer:
            return None  # boundary violation
        else:
            return self.Position(self, node)  # legitimate position

    #-----------accessors------------------
    def first(self):
        '''return first position in list or None if empty'''
        return self._make_position(self._header._next)

    def last(self):
        '''return last position in list or None if empty'''
        return self._make_position(self._trailer._prev)

    def before(self, p):
        '''return position just before position p or None if p is first'''
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        '''return postition just after p or None if p is last'''
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        '''generate a forward iteration of elements in the lsit'''
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    #---------mutators------------------
    # override inherited version to return Position rather than Node
    def _insert_between(self, e, predecessor, successor):
        '''add element between two elements'''
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        '''insert element at front of list'''
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        '''insert element at back of list'''
        return self._insert_between(e, self._trailer,_prev, self._trailer)

    def add_before(self, p, e):
        '''insert element into list before p'''
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p, e):
        '''insert element into list after p'''
        original = self._validate(p)
        return self._insert_between(e, original, original._next)

    def delete(self, p):
        '''remove element at position p'''
        original = self._validate(p)
        return self._delete_node(original)  # inherited method returns element

    def replace(self, p, e):
        '''replace element at position p with e'''
        original = self._validate(p)
        old_value = original._element  # temp store old ele
        original._element = e  # replace
        return old_value  # return old ele
