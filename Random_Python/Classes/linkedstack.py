'''
    Stack implemented into linked list
'''
class LinkedStack:
    '''LIFO Stack implemented using a singly linked list for storage'''
    # -------------nested _Node class -----------
    class _Node:
        '''lightweight nonpublic clss for storing a singly linked node'''
        __slots__ = '_element', '_next'  # streamline memory

        def __init__(self, element, next):  # init first node
            self._element = element  # ref user's element
            self._next = next  # ref user's next

    # ---------- stack methods ---------------
    def __init__(self):
        '''create empty stack'''
        self._head = None  # ref head node
        self._size = 0  # num of stack elements

    def __len__(self):
        '''return num elements'''
        return self._size

    def is_empty(self):
        '''return True if empty'''
        return self._size == 0

    def push(self, e):
        '''add element e to top of stack'''
        self._head = self._Node(e, self._head)  # create and link new node
        self._size += 1

    def top(self):
        '''return but do not remove top element

        raise exception if empty
        '''
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element  # top stack is at head

    def pop(self):
        '''remove and return top element

        raise exception if empty
        '''
        if self.is_empty():
            raise Empty('Stack is empty')
        answer = self._head._element
        self._head = self._head._next  # bypass former top
        self._size -= 1
        return answer
