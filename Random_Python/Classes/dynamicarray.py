'''
    Mimicing a list type class
    Dynamic array
'''
import ctypes  # provides access to low-level arrays


class DynamicArray:
    '''similar to list where it can grow as needed'''


    def __init__(self):
        '''create empty array'''
        self._n = 0  # count elements
        self._capacity = 1  # default capacity
        self._A = self._make_array(self._capacity)  # low level array using ctypes

    def __len__(self):
        '''return num of elements stored in array'''
        return self._n

    def __getitem__(self, k):
        '''return element at index k'''
        if not 0 <= k < self._n:
            raise IndexError('Invalid index')
        return self._A[k]  # retrieve from array

    def append(self, obj):
        '''add object to end of array'''
        if self._n == self._capacity:  # not enough room
            self._resize(2 * self._capacity)  # double the capacity
        self._A[self._n] = obj
        self._n += 1

    def resize(self, c):  # non public utility
        '''resize internal array to capacity c'''
        B = self._make_array(c)  # new bigger array
        for k in range(self._n):  # for each existing element
            B[k] = self._A[k]
        self._A = B  # use bigger array
        self._capacity = c

    def _make_array(self, c):  # non public utility
        '''return new array with capacity c'''
        return (c * ctypes.py_object)()  # ctypes docs explains

