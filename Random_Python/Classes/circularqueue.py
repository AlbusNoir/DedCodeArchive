'''
    queue implementation using circularly linked list for storage
'''
class CircularQueue:



    class _Node:
        # same as other list implementations
        # nonpublic class for singly linked node

    def __init__(self):
        '''empty queue'''
        self._tail = None  # tail ele
        self._size = 0  # num eles

    def __len__(self):
        '''num eles'''
        return self._size

    def is_empty(self):
        '''True if empty, else False'''
        return self._size == 0

    def first(self):
        '''first ele'''
        if is_empty():
            raise Empty('Queue is empty')
        head = self._tail._next
        return head._element

    def dequeue(self):
        '''remove first ele'''
        if self.is_empty():
            raise Empty('Queue is empty')
        oldhead = self._tail._next
        if self._size == 1:  # rem only ele
            self._tail = None  # queue empty
        else:
            self._tail._next = oldhead._next  # bypass old head
        self._size -= 1
        return oldhead._element

    def enqueue(self, e):
        '''add ele to back of queue'''
        newest = self._Node(e, None)  # node new tail
        if self.is_empty():
            newest._next = newest  # initialize circularly
        else:
            newest._next = self._tail._next  # new node points to head
            self._tail._next = newest  # old tail points to new node
        self._tail = newest  # new node is tail
        self._size += 1

    def rotate(self):
        '''rotate front ele to back of queue'''
        if self._size > 0:
            self._tail = self._tail._next  # old head becomes tail
