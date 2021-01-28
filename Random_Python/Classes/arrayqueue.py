'''
    Mimic array queue
    FIFO using list as underlying storage
'''

class ArrayQueue:
    '''FIFO mimic using list as underlying storage'''
    DEFAULT_CAPACITY = 10  # moderate capacity for all new queues

    def __init__(self):
        '''create empty queue'''
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        '''return num of elements in queue'''
        return self._size

    def is_empty(self):
        '''return True if queue is empty'''
        return self._size == 0

    def first(self):
        '''return but do not remove front element of queue

        raise Empty exception if empty
        '''
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        '''remove and return first element of queue
        FIFO

        raise Empty is queue is empty
        '''
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None  # garbage collection
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, e):
        '''add element to back of queue'''
        if self._size == len(self._data):
            self._resize(2 * len(self._data))  # double size
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):
        '''resize to a new list of capacity >= len(self)

        assume cap >= len(self)
        '''
        old = self._data  # existing list
        self._data = [None] * cap  # allocate list with new capacity
        walk = self._front
        for k in range(self._size):  # only consider existing elements
            self._data[k] = old[walk]  # shift indices
            walk = (1 + walk) % len(old)  # use old size as modulus
        self._front = 0  # front has been realigned
