'''
    implementation of a queue using a singly linked list as storage
'''
class LinkedQueue:


    class _Node:
        '''nonpublic node class'''
        # reference LinkedStack for this node class

    def __init__(self):
        '''empty queue'''
        self._head = None
        self._tail = None
        self._size = 0  # num of queue ele

    def __len__(self):
        '''return num ele'''
        return self._size

    def is_empty(self):
        '''True is empty, else False'''
        return self._size == 0

    def first(self):
        '''return front queue ele'''
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._head._element

    def dequeue(self):
        '''return first element and remove(FIFO)'''
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None  # special case if queue is now empty, remove tail
        return answer

    def enqueue(self, e):
        '''add element to back of queue'''
        newest = self._Node(e, None)  # new node will be tail
        if self.is_empty():
            self._head = newest  # if was empty, node is now head
        else:
            self._tail._next = newest
        self._tail = newest  # update tail ref
        self._size += 1
