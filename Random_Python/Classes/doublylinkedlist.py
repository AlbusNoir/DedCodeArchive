'''
    Doubly linked list
'''
class DoublyLinkedBase:

    class _Node:
        '''nonpublic node class'''
        __slots__ = '_element', '_prev', '_next'

    def __init__(self):
        '''create empty list'''
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer  # trailer after header
        self._trailer._prev = self._header  # header before trailer
        self._size = 0

    def __len__(self):
        '''num eles'''
        return self._size

    def is_empty(self):
        '''True if empty, else False'''
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        '''add an element between two existing nodes and return new node'''
        newest = self._Node(e, predecessor, successor)  # linked to neighbouring nodes
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        '''delete nonsentinel node and return element'''
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element  # record deleted ele
        node._prev = node._next = node._element = None  # deprecate node
        return element  # return ele
