'''Abstract class
    mimics collections.Sequence
'''
from abc import ABCMeta, abstractmethod


class Sequence(metaclass=ABCMeta):
    '''mimics collections.Sequence'''

    @abstractmethod
    def __len__(self):
        '''returns length of sequence'''

    @abstractmethod
    def __getitem__(self, j):
        '''returns element at index j of sequence'''

    def __contains__(self, val):
        '''return True if val found in sequence; otherwise False'''
        for j in range(len(self)):
            if self[j] == val:
                # match
                return True
        return False  # otherwise

    def index(self, val):
        '''return leftmost index at which val is found
        otherwise raise ValueError
        '''
        for j in range(len(self)):
            if self[j] == val:  # leftmost match
                return j
        raise ValueError('Value not in sequence')  # no match

    def count(self, val):
        '''return the number of elements equal to given value'''
        k = 0
        for j in range(len(self)):
            if self[j] == val:  # match
                k += 1
        return k
