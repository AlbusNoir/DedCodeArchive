'''
    Mimic stack
'''


class ArrayStack:
    '''LIFO stack using list as underlying storage'''

    def __init__(self):
        '''create empty stack'''
        self._data = []  # nonpublic list instance

    def __len__(self):
        '''return num of elements in stack'''
        return len(self.data)

    def is_empty(self):
        '''return True if empty'''
        return len(self._data) == 0

    def push(self, e):
        '''add element to top of stack'''
        self._data.append(e)  # new element stored at end of list

    def top(self):
        '''return but do not remove element at top of stack

        raise Empty exception if empty
        '''
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]  # last item in list

    def pop(self):
        '''remove and return element from top of stack (LIFO)

        raise Empty exception if stack is emtpy
        '''
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()  # remove last item from list
